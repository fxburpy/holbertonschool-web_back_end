#!/usr/bin/env python3
"""
Bu modül, asenkron fonksiyonların paralel çalıştırılma
süresini ölçen bir coroutine içerir.
"""

import asyncio
import time

# Bir önceki görevden async_comprehension fonksiyonunu içe aktarıyoruz
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension fonksiyonunu asyncio.gather kullanarak 4 kez
    paralel olarak çalıştırır ve toplam geçen süreyi hesaplar.
    """
    start_time = time.perf_counter()

    # 4 görevi bir liste içinde oluşturup * operatörü ile unpack ediyoruz
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    return end_time - start_time
