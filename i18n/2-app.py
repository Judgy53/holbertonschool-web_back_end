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


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Find the best locale from request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"])
def index() -> str:
    """ GET /

    Returns :
    - 2-index.html
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
