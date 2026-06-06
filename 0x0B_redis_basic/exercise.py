#!/usr/bin/env python3
"""
Module for caching data in Redis
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method of the Cache class is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function to increment call count and execute method """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function to append inputs and outputs to redis lists """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        # Store the input arguments as a string representation
        self._redis.rpush(input_key, str(args))
        
        # Execute the original method to get the output
        output = method(self, *args, **kwargs)
        
        # Store the output
        self._redis.rpush(output_key, str(output))
        
        return output
        
    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function.
    """
    redis_client = redis.Redis()
    name = method.__qualname__
    
    # Get the number of calls
    calls = redis_client.get(name)
    try:
        calls = int(calls.decode("utf-8"))
    except (AttributeError, ValueError):
        calls = 0

    print(f"{name} was called {calls} times:")
    
    # Retrieve the inputs and outputs from Redis
    inputs = redis_client.lrange(f"{name}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{name}:outputs", 0, -1)
    
    # Zip them together and print
    for i, o in zip(inputs, outputs):
        try:
            i_str = i.decode("utf-8")
        except AttributeError:
            i_str = ""
            
        try:
            o_str = o.decode("utf-8")
        except AttributeError:
            o_str = ""
            
        print(f"{name}(*{i_str}) -> {o_str}")


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

    @count_calls
    @call_history
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis. If a callable function is provided, 
        applies it to the retrieved data.

        Args:
            key (str): The key to search for in Redis.
            fn (Optional[Callable]): The function to apply to the retrieved data.

        Returns:
            The data in its original type, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string value from Redis.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis.
        """
        return self.get(key, fn=int)