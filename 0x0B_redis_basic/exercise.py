#!/usr/bin/env python3
""" Cache module
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Redis Cache Class
    """
    def __init__(self) -> None:
        """ Constructor for the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store `data` in redis using a random key.
        Returns the generated key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
