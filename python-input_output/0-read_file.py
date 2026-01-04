#!/usr/bin/python3
"""Read and print UTF-8 text file."""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): Path to the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
