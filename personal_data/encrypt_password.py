#!/usr/bin/env python3
"""
Module that provides helper functions to encrypt passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Salts and hash a password"""
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if provided password matches the hashed password"""
    return bcrypt.checkpw(str.encode(password), hashed_password)
