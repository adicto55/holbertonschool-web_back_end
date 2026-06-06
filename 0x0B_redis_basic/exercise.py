#!/usr/bin/env python3
"""
Module for caching data in Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for interacting with a Redis database.
    """
    def __init__(self):
        """
        Initialize the Cache instance.
        Stores an instance of the Redis client as a private variable and 
        flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in Redis using the key,
        and returns the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key