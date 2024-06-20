#!/usr/bin/env python3
""" Module of Session Auth views
"""
from flask import abort, jsonify, request
from os import getenv
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if email or password is missing or empty
      - 404 if user doesn't exist
      - 401 if password isn't valid
    """
    email = request.form.get("email")
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    user_search = User.search({"email": email})
    if user_search is None or len(user_search) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = user_search[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session = auth.create_session(user.id)

    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session)
    return response
