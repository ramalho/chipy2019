#!/usr/bin/env python3

# spin_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_THREAD
import threading
import itertools
import time


def spin(msg, computation):  # <1>
    for char in itertools.cycle('⠇⠋⠙⠸⠴⠦'):  # <3>
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        if computation.wait(.1):  # <5>
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow_function():  # <7>
    # pretend waiting a long time for I/O
    time.sleep(3)  # <8>
    return 42


def supervisor():  # <9>
    computation = threading.Event()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', computation))
    print('spinner object:', spinner)  # <10>
    spinner.start()  # <11>
    result = slow_function()  # <12>
    computation.set()  # <13>
    spinner.join()  # <14>
    return result


def main():
    result = supervisor()  # <15>
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_THREAD
