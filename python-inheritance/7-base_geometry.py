#!/usr/bin/python3
class BaseGeometry:
    """A base geometry class with area and integer_validator methods"""
    
    def area(self):
        """Raise an exception - area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0"""
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
