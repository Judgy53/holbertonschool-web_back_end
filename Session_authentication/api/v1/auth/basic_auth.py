#!/usr/bin/env python3
""" Basic Authorization module
"""
import base64
import binascii
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authorization class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the base64 part of the auth header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Decodes the base64 part of the auth header"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header,
                                       validate=True)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """Extracts the user credentials from the decoded header"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        separator_index = decoded_base64_authorization_header.find(":")
        if separator_index == -1:
            return (None, None)

        email = decoded_base64_authorization_header[:separator_index]
        password = decoded_base64_authorization_header[separator_index + 1:]
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Find the user object in the database from the credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            user_search = User.search({'email': user_email})
        except Exception:
            return None

        for user in user_search:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current logged user"""
        auth_header = self.authorization_header(request)
        b64_auth = self.extract_base64_authorization_header(auth_header)
        decoded_auth = self.decode_base64_authorization_header(b64_auth)
        email, password = self.extract_user_credentials(decoded_auth)
        return self.user_object_from_credentials(email, password)
