#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits BaseCaching and implements:
      - putting data in the cache (max BaseCaching.MAX_ITEMS items)
      - discard least frequency (LRU if multiple) used item if over capacity
      - getting data from the cache
    """

    def __init__(self):
        """ Initialize the lfu cache
        """
        self.freq_data = {}
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.freq_data:
            del self.cache_data[key]
        else:
            self.freq_data[key] = -1

        self.cache_data[key] = item
        self.freq_data[key] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.find_lfu_key(key)
            print('DISCARD: ' + discard)
            del self.cache_data[discard]
            del self.freq_data[discard]

    def find_lfu_key(self, just_inserted_key):
        lfu_key = None
        lfu_freq = float('inf')
        for key in iter(self.cache_data):
            if key == just_inserted_key:
                continue

            freq = self.freq_data[key]
            if freq < lfu_freq:
                lfu_key = key
                lfu_freq = freq

        return lfu_key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        val = self.cache_data.pop(key)
        self.cache_data[key] = val
        self.freq_data[key] += 1

        return val
