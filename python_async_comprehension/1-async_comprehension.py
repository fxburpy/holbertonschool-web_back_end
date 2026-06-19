#!/usr/bin/env python3
"""
Bu modül, asenkron liste kavrayışı (async comprehension)
kullanarak veri toplayan bir coroutine içerir.
"""

from typing import List

# Bir önceki görevden async_generator fonksiyonunu içe aktarıyoruz
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_generator üzerinden asenkron bir liste kavrayışı gerçekleştirir,
    üretilen 10 rastgele sayıyı toplar ve bir liste olarak döndürür.
    """
    return [i async for i in async_generator()]
