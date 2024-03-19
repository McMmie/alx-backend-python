#!/usr/bin/env python3
"""
an async generator
"""
import asyncio
from random import uniform


async def async_generator():
    """
    generates a random number between 0 and 10
    """
    for i in range(11):
        await asyncio.sleep(1)
        yield uniform(0, 10)
