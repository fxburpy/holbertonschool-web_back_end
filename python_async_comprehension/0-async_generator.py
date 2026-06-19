#!/usr/bin/env python3
"""
Bu modül, asenkron bir jeneratör fonksiyonu ve doğru tip
tanımlamalarını (type annotations) içerir.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    10 kez döngü kurar, her seferinde asenkron olarak 1 saniye bekler
    ve 0 ile 10 arasında rastgele bir sayı döndürür (yield).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
