#!/usr/bin/env python3
""" Web module
"""
import redis
import requests
from typing import Callable
from functools import wraps

redis_instance = redis.Redis()


def cache_and_count(method: Callable) -> Callable:
    """ Decorator that count calls and cache the result for 10 seconds
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Wrapper to the method
        """
        url = args[0]
        redis_instance.incr('count:{}'.format(url))
        cached = redis_instance.get('cached:{}'.format(url))
        if cached:
            return cached.decode('utf-8')

        out = method(*args, **kwargs)
        redis_instance.setex('cached:{}'.format(url), 10, out)
        return out
    return wrapper


@cache_and_count
def get_page(url: str) -> str:
    """ Request a url and return its HTML content
    """
    return requests.get(url).text
