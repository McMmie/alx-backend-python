#!/usr/bin/env python3
"""
how to antonate callables
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """antonates a function
    """

    def mult(x: float) -> float:
        """this is the callable function
        """

        return x * multiplier

    return mult
