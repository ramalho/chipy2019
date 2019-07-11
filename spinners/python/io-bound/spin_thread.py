#!/usr/bin/env python3

# spin_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN DOWNLOAD_THREAD
import threading
import itertools
import time
from urllib import request


import images

def spin(msg, downloaded):  # <1>
    for char in itertools.cycle('⠇⠋⠙⠸⠴⠦'):  # <3>
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        if downloaded.wait(.1):  # <5>
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')



def fetch(url):
    with request.urlopen(url) as req:
        assert req.status == 200
        return req.read()


def fetch_by_size(target_size):
    size, path = images.pick_by_size(target_size)
    url = images.BASE_URL + path 
    
    octets = fetch(url)
    
    name = images.save(url, octets)
    return (size, name)


def slow_function():
    return fetch_by_size(7_000_000)


def supervisor():  # <9>
    downloaded = threading.Event()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', downloaded))
    print('spinner object:', spinner)  # <10>
    spinner.start()  # <11>
    result = slow_function()  # <12>
    downloaded.set()  # <13>
    spinner.join()  # <14>
    return result


def main():
    t0 = time.perf_counter()
    size, name = supervisor()  # <15>
    dt = time.perf_counter() - t0
    print(f'{size:_d} bytes downloaded')
    print('File name:', name)
    print(f'Elapsed time: {dt:0.3}s')

if __name__ == '__main__':
    main()
# END SPINNER_THREAD
