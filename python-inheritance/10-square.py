#!/usr/bin/python3
"""Module for Square class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size."""
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
