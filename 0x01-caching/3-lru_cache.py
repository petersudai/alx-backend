#!/usr/bin/python3
"""
class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
