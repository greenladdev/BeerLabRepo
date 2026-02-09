import os
import random

from flask import Flask, abort, render_template

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

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
