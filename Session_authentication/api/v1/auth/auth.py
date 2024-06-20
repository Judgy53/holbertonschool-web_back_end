#!/usr/bin/env python3
""" Authorization module
"""
from os import getenv
from flask import request
from typing import TypeVar, List


class Auth():
    """Authorization class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authorization"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded in excluded_paths:
            if path == excluded:
                return False

            if excluded.endswith('*'):
                partial = excluded[:-1]
                if path.startswith(partial):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get the value of the request header Authorization"""
        if request is None or "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the auth user data"""
        return None

    def session_cookie(self, request=None):
        """Get the session cookie from the request"""
        if request is None:
            return None

        return request.cookies.get(getenv("SESSION_NAME"))
