#!/usr/bin/env python3
""" Database Session Authorization module
"""
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Database Session Authorization class
    """

    def create_session(self, user_id=None) -> str:
        """Create an expirable session ID for a user_id"""
        session = super().create_session(user_id)
        if session is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session)
        user_session.save()

        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user ID based on the session_id"""

        user_search = UserSession.search({"session_id": session_id})

        if user_search is None or len(user_search) == 0:
            return None

        return super().user_id_for_session_id(session_id)

    def destroy_session(self, request=None) -> bool:
        """Attempt to destroy the user current session"""
        if request is None:
            return None

        session = self.session_cookie(request)
        if session is None:
            return False

        user_search = UserSession.search({"session_id": session})

        if user_search is None or len(user_search) == 0:
            return False

        user_search[0].remove()
        return super().destroy_session(request)
