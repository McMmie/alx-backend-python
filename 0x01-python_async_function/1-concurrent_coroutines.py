#!/usr/bin/env python3
"""
documentation
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    documentation needed
    """

    wait_times = await asyncio.gather(
            *[wait_random(max_delay) for _ in range(n)]
            # *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
