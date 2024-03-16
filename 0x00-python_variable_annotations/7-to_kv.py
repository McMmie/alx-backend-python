#!/usr/bin/env python3
"""
converts string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple after a couple of aruthmatic expression
    and returns a tuple
    """
    return (k, float(v ** v))
