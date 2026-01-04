#!/usr/bin/python3
"""Module for safe integer printing"""


def safe_print_integer(value):
    """Print an integer with {:d} format and return True if successful"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
