#!/usr/bin/env python3
"""
Module documentation: 0-basic_async_syntax
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine: wait_random

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay between 0 and max_delay (inclusive).
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
