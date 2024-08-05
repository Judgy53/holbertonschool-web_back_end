#!/usr/bin/env python3
""" Cache module
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable, TypeVar

T = TypeVar("T")


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

    def get(self, key: str, fn: Optional[Callable[..., T]]) -> T:
        """ Retrieve data with `key` and converts it using `fn`.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """ Retrieve data with `key` and converts it to UTF-8 string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Retrieve data with `key` and converts it to int.
        """
        return self.get(key, int)
