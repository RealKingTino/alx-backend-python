#!/usr/bin/env python3
"""
Module documentation: 4-tasks
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """
    Create a list of asyncio.Tasks for wait_random(max_delay) calls.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[asyncio.Task]: List of tasks representing the execution of wait_random(max_delay).
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
