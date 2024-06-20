#!/usr/bin/env python3
""" Expirable Session Authorization module
"""
from os import getenv
import datetime
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Expirable Session Authorization class
    """
    def __init__(self) -> None:
        duration = getenv("SESSION_DURATION")

        try:
            if duration is None:
                raise Exception
            self.session_duration = int(duration)
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """Create an expirable session ID for a user_id"""
        session = super().create_session(user_id)
        if session is None:
            return None

        self.user_id_by_session_id[session] = {
            "user_id": user_id,
            "created_at": datetime.datetime.now()
        }

        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user ID based on the session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None

        user = self.user_id_by_session_id.get(session_id)
        if user is None:
            return None

        if self.session_duration <= 0:
            return user["user_id"]

        if "created_at" not in user:
            return None

        max_duration = datetime.timedelta(seconds=self.session_duration)
        expired_time = user["created_at"] + max_duration
        if expired_time < datetime.datetime.now():
            return None

        return user["user_id"]
