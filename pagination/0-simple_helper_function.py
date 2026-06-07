#!/usr/bin/env python3
"""
Module containing the index_range helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the given pagination parameters.
    
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
        
    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    
    return (start_index, end_index)