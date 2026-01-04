#!/usr/bin/python3
"""Module for safe list of integers printing"""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers"""
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed
