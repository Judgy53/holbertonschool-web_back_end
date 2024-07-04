#!/usr/bin/env python3
""" App module
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """ GET /

    Returns :
    - 0-index.html
    """
    return render_template("0-index.html")
