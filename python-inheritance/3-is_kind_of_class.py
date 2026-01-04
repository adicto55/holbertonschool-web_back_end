#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherited from it, otherwise False"""
    return isinstance(obj, a_class)
