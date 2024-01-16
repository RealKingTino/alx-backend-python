#!/usr/bin/env python3
"""
Module documentation: 1-concurrent_coroutines
"""

import asyncio
from typing import List

# Importing the wait_random coroutine from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine: wait_n

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
