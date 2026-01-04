#!/usr/bin/python3
"""Create an Object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename (str): Path to the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
