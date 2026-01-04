#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False"""
    return type(obj) is a_class
