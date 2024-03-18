#!/usr/bin/env python3
"""
documentation
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> float:
    """
    documentation needed
    """

    wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
