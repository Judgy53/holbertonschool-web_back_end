#!/usr/bin/env python3
"""App module
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ POST /sessions

    JSON body :
        - email
        - password

    Returns :
        - {"email": "<registered email>", "message": "logged in"}, 400
        - 401 if login info is incorrect
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    session = AUTH.create_session(email)

    out = jsonify({"email": email, "message": "logged in"})
    out.set_cookie('session_id', session)
    return out


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ DELETE /sessions

    Required cookies:
        - session_id

    Returns:
        - Redirect to "GET /"
        - 403 if user doesn't exist
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """ GET /profile

    Required cookies:
        - session_id

    Returns:
        - {"email": "<user email>"}, 200
        - 403 if session_id is invalid or user not found
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """ POST /reset_password

    JSON Body:
        - email

    Returns:
        - {"email": "<user email>", "reset_token": "<reset token>"}, 200
        - 403 if email is missing or user not found
    """
    email = request.form.get("email")

    if email is None:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route("/update_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """ PUT /update_password

    JSON Body:
        - email
        - reset_token
        - new_password

    Returns:
        - {"email": "<user email>", "message": "Password updated"}, 200
        - 403 if any field is missing or token is invalid
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    if email is None or reset_token is None or new_password is None:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
