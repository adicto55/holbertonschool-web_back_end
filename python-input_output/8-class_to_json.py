#!/usr/bin/python3
"""Return the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
