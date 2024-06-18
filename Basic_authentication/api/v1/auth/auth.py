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
        return False

    def authorization_header(self, request=None) -> str:
        """Get the value of the header request Authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the auth user data"""
        return None
