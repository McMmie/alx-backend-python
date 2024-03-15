#!/usr/bin/env python3
"""
a module for list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of all the floats in a list
    as a float
    """

    num = 0

    for item in input_list:
        num += item

    return float(num)
