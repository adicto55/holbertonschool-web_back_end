#!/usr/bin/env python3
"""
Module that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic searched.

    Returns:
        A list of school documents containing the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))