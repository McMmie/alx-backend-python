#!/usr/bin/env python3
"""
measuring the runtime for four parallel comprehensions
"""
import asyncio
from time import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime and return it.
    """
    start: float = time()
    await asyncio.gather(*[async_comp() for _ in range(4)])
    return time() - start
