#!/usr/bin/env python3
""" Session Authorization module
"""
import uuid
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authorization class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def destroy_session(self, request=None) -> bool:
        """Attempt to destroy the user current session"""
        if request is None:
            return None

        session = self.session_cookie(request)
        if session is None:
            return False

        user = self.user_id_for_session_id(session)
        if user is None:
            return False

        self.user_id_by_session_id.pop(session)
        return True

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user ID based on the session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the auth user data"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
