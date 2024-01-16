#!/usr/bin/env python3
"""
Module documentation: 3-tasks

This module contains a function, task_wait_random, which takes an integer max_delay and returns an asyncio.Task.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task representing the execution of wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
