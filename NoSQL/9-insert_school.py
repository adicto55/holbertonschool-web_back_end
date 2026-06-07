#!/usr/bin/env python3
"""
Module that inserts a new document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields and values to insert as a document.

    Returns:
        The new document's _id.
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id