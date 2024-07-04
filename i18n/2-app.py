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
    """ Get best locale from request
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def index() -> str:
    """ GET /

    Returns :
    - 0-index.html
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
