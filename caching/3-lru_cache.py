#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits BaseCaching and implements:
      - putting data in the cache (max BaseCaching.MAX_ITEMS items)
      - discard least recently used item if over capacity
      - getting data from the cache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            print('DISCARD: ' + discard)
            del self.cache_data[discard]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        val = self.cache_data.pop(key)
        self.cache_data[key] = val

        return val
