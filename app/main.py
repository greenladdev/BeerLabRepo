import os
import random

from flask import Flask, abort, render_template

from app.data import OFF_FLAVORS, get_flavor_by_slug


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
        return render_template("index.html", flavors=OFF_FLAVORS)

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
