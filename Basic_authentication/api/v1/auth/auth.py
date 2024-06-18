#!/usr/bin/env python3
""" Authorization module
"""
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

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Get the value of the request header Authorization"""
        if request is None or "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the auth user data"""
        return None
