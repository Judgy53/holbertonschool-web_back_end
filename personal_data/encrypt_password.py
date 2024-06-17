#!/usr/bin/env python3
"""
Module that provides helper functions to encrypt passwords
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Salts and hash a password"""
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
