#!/usr/bin/env python3
"""
Bu modül, asenkron bir jeneratör (async generator) fonksiyonu içerir.
"""

import asyncio
import random


async def async_generator():
    """
    10 kez döngü kurar, her seferinde asenkron olarak 1 saniye bekler
    ve 0 ile 10 arasında rastgele bir sayı döndürür (yield).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
