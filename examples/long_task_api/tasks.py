import asyncio
import time
from random import random


async def execute_async_cpu(load_factor: int = 9) -> int:
    return execute_sync_cpu(load_factor)


async def execute_async_io(load_factor: int = 9) -> float:
    seconds = random() * (10 ** (load_factor - 7)) / 2
    await asyncio.sleep(seconds)
    return seconds


def execute_sync_cpu(load_factor: int = 9) -> int:
    iterations = int(random() * (10**load_factor))
    acc = 0
    for i in range(iterations):
        acc += i
        acc %= 1000
    return acc


def execute_sync_io(load_factor: int = 9) -> float:
    seconds = random() * (10 ** (load_factor - 7)) / 2
    time.sleep(seconds)
    return seconds
