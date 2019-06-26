#!/usr/bin/env python3

"""
Allen's tasks:

1. Eat breakfast
2. Work
3. Eat lunch
4. Call Bob


Bob's tasks:

1. Eat breakfast
2. Wait for a call
3. Eat lunch
"""

import threading
import random
import time

from threading_cleanup import Thread


def show(name, activity):
    time.sleep(random.random() / 10)
    print(name, activity, sep=':\t', flush=True)


def allen_day(call):
    show('Allen', '☕\tEating breakfast')
    show('Allen', '🛠\tWorking')
    show('Allen', '🌮\tEating lunch')
    show('Allen', '📞\tCall Bob')
    call.set()


def bob_day(call):
    show('Bob', '☕\tEating breakfast')
    show('Bob', '🕰\tWaiting for a call')
    call.wait()
    show('Bob', '🍔\tEating lunch')


def main():
    call = threading.Event()
    Thread(allen_day, call)
    Thread(bob_day, call)

main()