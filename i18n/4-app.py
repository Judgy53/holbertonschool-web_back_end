#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ App Config Class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """ Find the best locale from request
    """
    locale = request.args.get("locale")
    if (locale is not None and locale in app.config["LANGUAGES"]):
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route("/", methods=["GET"])
def index() -> str:
    """ GET /

    Returns :
    - 4-index.html
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
