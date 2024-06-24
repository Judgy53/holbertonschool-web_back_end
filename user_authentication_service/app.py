#!/usr/bin/env python3
"""App module
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def index() -> str:
    """ GET /

    Returns :
    - {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST /users

    JSON body :
        - email
        - password

    Returns :
        - {"email": "<registered email>", "message": "user created"}
        - if the email or password is missing:
            - {"message": "email and password are required fields"}
            - 400
        - if the user is already registered:
            - {"message": "email already registered"}
            - 400
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
