#!/usr/bin/env python3
"""
complex types - mixed list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sum of a mixed list as a float
    """

    num = 0
    for item in mxd_lst:
        num += item

    return float(num)
