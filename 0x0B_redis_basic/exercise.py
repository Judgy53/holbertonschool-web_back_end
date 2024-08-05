#!/usr/bin/env python3
""" Cache module
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable, TypeVar
from functools import wraps

T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """ Decorator that count calls to the method and store it in the cache.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to the method
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator that record inputs and outputs and store it in the cache
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to the method
        """
        self._redis.rpush('{}:inputs'.format(method.__qualname__),
                          str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush('{}:outputs'.format(method.__qualname__),
                          str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """ Prints the history of calls of a method.
    """
    cache = Cache.instance
    name = method.__qualname__
    count = cache.get_int(name)
    inputs = cache._redis.lrange('{}:inputs'.format(name), 0, -1)
    outputs = cache._redis.lrange('{}:outputs'.format(name), 0, -1)

    print('{} was called {} times:'.format(name, count))
    for (i, o) in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(name,
                                     i.decode('utf-8'), o.decode('utf-8')))


class Cache:
    """ Redis Cache Class
    """
    instance: 'Cache' = None

    def __init__(self) -> None:
        """ Constructor for the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
        Cache.instance = self

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store `data` in redis using a random key.
        Returns the generated key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[..., T]] = None) -> T:
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
