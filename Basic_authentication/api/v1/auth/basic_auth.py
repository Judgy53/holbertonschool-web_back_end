#!/usr/bin/env python3
""" Basic Authorization module
"""
import base64
import binascii
from typing import Tuple
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
        except binascii.Error:
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
