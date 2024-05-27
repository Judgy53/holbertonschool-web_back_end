#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits BaseCaching and implements:
      - putting data in the cache (max BaseCaching.MAX_ITEMS items)
      - discard first item put in the cache if over capacity
      - getting data from the cache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
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

        return self.cache_data[key]
