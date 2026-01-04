#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    
    def __init__(self, size):
        """Initialize a Square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
    
    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
