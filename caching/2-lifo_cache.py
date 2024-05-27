#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits BaseCaching and implements:
      - putting data in the cache (max BaseCaching.MAX_ITEMS items)
      - discard last item put in the cache if over capacity
      - getting data from the cache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem()
            print('DISCARD: ' + discard)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
