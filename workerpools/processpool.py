from concurrent import futures
import math
import time

NUMBERS = [
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    65956211*65956229,
    49468369*49468387,
    ]

def is_prime(n):
    t0 = time.perf_counter()
    if n % 2 == 0:
        return (False, time.perf_counter() - t0)

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return (False, time.perf_counter() - t0)
    return (True, time.perf_counter() - t0)

def main():
    with futures.ProcessPoolExecutor() as executor:
        future_map = {executor.submit(is_prime, n): n
                      for n in NUMBERS}
        for future in futures.as_completed(future_map):
            n = future_map[future]
            res, dt = future.result()
            msg = 'is' if res else 'is not'
            print(f'({dt:0.3f}s) {n:18d} {msg} prime')

if __name__ == '__main__':
    main()
