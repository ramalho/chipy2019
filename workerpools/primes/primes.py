#!/usr/bin/env python3

import math

NUMBERS = [
                   2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
                   3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
                   5,  # prime
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    import time

    t0 = time.perf_counter()
    for n in NUMBERS:
        prime = '  # prime' if is_prime(n) else ''
        print(f'    {n:16d},{prime}')

    dt = time.perf_counter() - t0
    print(f'Total time: {dt:0.3f}s')

