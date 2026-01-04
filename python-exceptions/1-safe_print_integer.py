#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with {:d} format and return True if successful"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
