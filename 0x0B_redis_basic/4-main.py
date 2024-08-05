#!/usr/bin/env python3
""" Main file """

exercise = __import__('exercise')
Cache = exercise.Cache

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)
exercise.replay(cache.store)
