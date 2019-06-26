#!/usr/bin/env python3

# spin_proc.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN PRIME_PROCESS
import multiprocessing
import itertools
import time
import primes


def spin(msg, computation):  # <1>
    for char in itertools.cycle('⠇⠋⠙⠸⠴⠦'):  # <3>
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        if computation.wait(.1):  # <5>
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow_function():
    return primes.is_prime(3033700317376073)


def supervisor():  # <9>
    computation = multiprocessing.Event()
    spinner = multiprocessing.Process(target=spin,
                               args=('thinking!', computation))
    print('spinner object:', spinner)  # <10>
    spinner.start()  # <11>
    result = slow_function()  # <12>
    computation.set()  # <13>
    spinner.join()  # <14>
    return result


def main():
    t0 = time.perf_counter()
    result = supervisor()  # <15>
    dt = time.perf_counter() - t0
    print(f'Answer: {result}')
    print(f'Elapsed time: {dt:0.3}s')

if __name__ == '__main__':
    main()
# END SPINNER_THREAD
