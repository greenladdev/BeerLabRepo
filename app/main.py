import os
import random
import textwrap
from io import BytesIO

from flask import Flask, abort, render_template, send_file
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

from app.data import OFF_FLAVORS, get_flavor_by_slug


SULFUR_KEYWORDS = (
    "sulfur",
    "sulphur",
    "dms",
    "dimethyl sulfide",
    "hydrogen sulfide",
    "mercaptan",
    "skunky",
    "matchstick",
    "rotten egg",
)
OXIDATION_KEYWORDS = (
    "oxidation",
    "oxidized",
    "stale",
    "cardboard",
    "papery",
    "sherry",
    "trans-2-nonenal",
)
ESTER_KEYWORDS = (
    "ester",
    "isoamyl",
    "ethyl",
    "banana",
    "pear",
    "fruity",
)

STAGE_KEYWORDS = {
    "mash_boil": (
        "boil",
        "wort",
        "sparge",
        "mash",
        "kettle",
        "hot-side",
        "chill",
        "flameout",
    ),
    "fermentation": (
        "fermentation",
        "yeast",
        "lagering",
        "conditioning",
        "diacetyl rest",
        "attenuation",
        "pitch",
    ),
    "packaging": (
        "packaging",
        "bottle",
        "keg",
        "light",
        "oxygen",
        "transfer",
        "shelf",
        "distribution",
    ),
}

SYMPTOM_TAG_KEYWORDS = {
    "sulfur_egg": ("sulfur", "rotten egg", "matchstick"),
    "buttery": ("butter", "butterscotch", "diacetyl"),
    "green_apple": ("green apple", "acetaldehyde"),
    "vinegar_sour": ("vinegar", "acetic", "lactic", "sour"),
    "solventy_fruity": ("solvent", "fruity", "banana", "pear", "ester"),
    "papery_stale": ("papery", "cardboard", "stale", "oxidation"),
    "skunky_light": ("skunky", "lightstruck", "uv light", "light damage"),
    "smoky_phenolic": ("smoky", "phenolic", "medicinal", "band-aid"),
    "astringent_harsh": ("astringent", "tannic", "harsh", "rough hop"),
}

PROCESS_TAG_KEYWORDS = {
    "warm_fermentation": ("high fermentation temperature", "warm", "temperature"),
    "yeast_stress": ("stressed yeast", "underpitch", "pitch", "yeast health"),
    "oxygen_pickup": ("oxygen", "oxidation", "post-fermentation", "transfer"),
    "sanitation": ("sanitize", "contamination", "bacteria", "wild yeast"),
    "light_exposure": ("light", "uv", "sunlight", "fluorescent"),
    "old_hops": ("aged hops", "old hops", "stale hops"),
    "water_chlorine": ("chlorine", "chloramine", "campden"),
    "sparge_extraction": ("sparge", "oversparging", "high ph", "extraction"),
}


def infer_flavor_family(flavor: dict) -> str:
    """Classify a flavor into one of the filter families used by the UI."""
    text = " ".join(
        [
            flavor.get("slug", ""),
            flavor.get("name", ""),
            flavor.get("nickname", ""),
            flavor.get("description", ""),
        ]
    ).lower()

    if any(keyword in text for keyword in SULFUR_KEYWORDS):
        return "sulfur"
    if any(keyword in text for keyword in OXIDATION_KEYWORDS):
        return "oxidation"
    if any(keyword in text for keyword in ESTER_KEYWORDS):
        return "ester"
    return "other"


def build_flavor_library() -> list[dict]:
    """Attach UI metadata used for filtering/search on the index page."""
    library = []
    for flavor in OFF_FLAVORS:
        search_text = " ".join(
            [
                flavor["name"],
                flavor["nickname"],
                flavor["description"],
                " ".join(flavor["common_styles"]),
                flavor["avoidance"],
            ]
        ).lower()

        enriched = dict(flavor)
        enriched["family"] = infer_flavor_family(flavor)
        enriched["search_text"] = search_text
        library.append(enriched)

    return library


def infer_primary_stage(text: str, family: str) -> str:
    """Infer primary process stage where the fault is typically introduced/noticed."""
    scores = {
        stage: sum(1 for keyword in keywords if keyword in text)
        for stage, keywords in STAGE_KEYWORDS.items()
    }

    best_stage = max(scores, key=lambda stage: scores[stage])
    if scores[best_stage] > 0:
        return best_stage

    if family == "oxidation":
        return "packaging"
    if family in {"sulfur", "ester"}:
        return "fermentation"
    return "mash_boil"


def extract_tags(text: str, tag_map: dict[str, tuple[str, ...]]) -> list[str]:
    """Return matching tags from keyword map."""
    tags = []
    for tag, keywords in tag_map.items():
        if any(keyword in text for keyword in keywords):
            tags.append(tag)
    return tags


def build_diagnosis_profiles() -> list[dict]:
    """Profiles used by the process-stage diagnosis wizard scoring engine."""
    profiles = []
    for flavor in build_flavor_library():
        text = " ".join(
            [
                flavor["name"],
                flavor["nickname"],
                flavor["description"],
                flavor["avoidance"],
                " ".join(flavor["common_styles"]),
            ]
        ).lower()

        profiles.append(
            {
                "slug": flavor["slug"],
                "name": flavor["name"],
                "nickname": flavor["nickname"],
                "family": flavor["family"],
                "stage": infer_primary_stage(text, flavor["family"]),
                "symptom_tags": extract_tags(text, SYMPTOM_TAG_KEYWORDS),
                "process_tags": extract_tags(text, PROCESS_TAG_KEYWORDS),
                "common_styles": flavor["common_styles"],
                "why": flavor["description"],
                "avoidance": flavor["avoidance"],
            }
        )

    return profiles


def build_style_risk_heatmap() -> list[dict]:
    """Aggregate likely off-flavors per style with weighted risk intensity."""
    style_map: dict[str, dict[str, dict]] = {}

    for flavor in build_flavor_library():
        for idx, style in enumerate(flavor["common_styles"]):
            base_score = max(1, 3 - idx)
            style_bucket = style_map.setdefault(style, {})
            entry = style_bucket.get(flavor["name"])

            if not entry:
                style_bucket[flavor["name"]] = {
                    "name": flavor["name"],
                    "nickname": flavor["nickname"],
                    "family": flavor["family"],
                    "score": base_score,
                    "why": flavor["description"],
                }
            else:
                entry["score"] += base_score

    heatmap = []
    for style, entries_map in style_map.items():
        risks = sorted(
            entries_map.values(),
            key=lambda item: (-item["score"], item["name"]),
        )

        if not risks:
            continue

        max_score = risks[0]["score"]
        for risk in risks:
            ratio = risk["score"] / max_score if max_score else 0
            if ratio >= 0.67:
                risk["risk_level"] = "High"
                risk["risk_class"] = "risk-high"
            elif ratio >= 0.34:
                risk["risk_level"] = "Medium"
                risk["risk_class"] = "risk-medium"
            else:
                risk["risk_level"] = "Low"
                risk["risk_class"] = "risk-low"

        heatmap.append({"style": style, "risks": risks, "risk_count": len(risks)})

    return sorted(heatmap, key=lambda item: item["style"])


def build_flashcards():
    """Build one quiz card per off-flavor with 3 multiple-choice options."""
    all_names = [flavor["name"] for flavor in OFF_FLAVORS]
    cards = []

    for flavor in OFF_FLAVORS:
        distractors = [name for name in all_names if name != flavor["name"]]
        options = random.sample(distractors, 2) + [flavor["name"]]
        random.shuffle(options)
        cards.append(
            {
                "name": flavor["name"],
                "nickname": flavor["nickname"],
                "description": flavor["description"],
                "common_styles": flavor["common_styles"],
                "avoidance": flavor["avoidance"],
                "options": options,
            }
        )

    random.shuffle(cards)
    return cards


def build_study_sheet_rows(library: list[dict]) -> list[list[str]]:
    """Rows for study-sheet exports."""
    rows = []
    for flavor in library:
        rows.append(
            [
                flavor["name"],
                flavor["nickname"],
                flavor["family"].title(),
                flavor["description"],
                ", ".join(flavor["common_styles"]),
            ]
        )
    return rows


def build_troubleshooting_rows(library: list[dict]) -> list[list[str]]:
    """Rows for troubleshooting-guide exports."""
    rows = []
    for flavor in library:
        rows.append(
            [
                flavor["name"],
                flavor["family"].title(),
                ", ".join(flavor["common_styles"]),
                flavor["avoidance"],
            ]
        )
    return rows


def create_pdf_response(
    title: str, filename: str, headers: list[str], rows: list[list[str]]
):
    """Return simple printable PDF response with wrapped text entries."""
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER

    y = height - 54
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(36, y, title)
    y -= 18

    pdf.setFont("Helvetica", 8)
    pdf.drawString(36, y, "Generated by Beer Fault Finder")
    y -= 22

    for row in rows:
        entry_lines = []
        for idx, value in enumerate(row):
            label = headers[idx]
            line = f"{label}: {value}"
            wrapped = textwrap.wrap(line, width=105) or [line]
            entry_lines.extend(wrapped)

        needed_height = (len(entry_lines) * 10) + 12
        if y - needed_height < 36:
            pdf.showPage()
            y = height - 40
            pdf.setFont("Helvetica", 9)

        pdf.setFont("Helvetica", 9)
        for line in entry_lines:
            pdf.drawString(36, y, line)
            y -= 10

        y -= 6
        pdf.line(36, y, width - 36, y)
        y -= 10

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf",
    )


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", flavors=build_flavor_library())

    @app.route("/flavor/<slug>")
    def flavor_detail(slug: str):
        flavor = get_flavor_by_slug(slug)
        if not flavor:
            abort(404)
        return render_template("detail.html", flavor=flavor)

    @app.route("/flashcards")
    def flashcards():
        return render_template("flashcards.html", cards=build_flashcards())

    @app.route("/style-risk")
    def style_risk():
        return render_template("heatmap.html", style_risks=build_style_risk_heatmap())

    @app.route("/diagnosis-wizard")
    def diagnosis_wizard():
        return render_template("diagnosis.html", profiles=build_diagnosis_profiles())

    @app.route("/export/study-sheet.pdf")
    def export_study_sheet_pdf():
        library = build_flavor_library()
        headers = ["Flavor", "Nickname", "Family", "Description", "Common Beer Styles"]
        rows = build_study_sheet_rows(library)
        return create_pdf_response(
            "Beer Study Sheet",
            "beer-study-sheet.pdf",
            headers,
            rows,
        )

    @app.route("/export/troubleshooting-guide.pdf")
    def export_troubleshooting_pdf():
        library = build_flavor_library()
        headers = ["Flavor", "Family", "Common Beer Styles", "How To Avoid"]
        rows = build_troubleshooting_rows(library)
        return create_pdf_response(
            "Beer Troubleshooting Guide",
            "beer-troubleshooting-guide.pdf",
            headers,
            rows,
        )

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
