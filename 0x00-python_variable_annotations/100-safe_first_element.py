#!/usr/bin/env python3
"""
This is a module that provides a function for returning the first element
of a list, or None if the list is empty."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
