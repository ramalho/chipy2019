#!/usr/bin/env python3
 
"""
1.5.3 Mutual exclusion with messages

Like serialization, mutual exclusion can be implemented using message passing.
For example, imagine that you and Bob operate a nuclear reactor that you monitor from remote stations.
Most of the time, both of you are watching for warning lights,
but you are both allowed to take a break for lunch.
It doesn’t matter who eats lunch first,
but it is very important that you don’t eat lunch at the same time,
leaving the reactor unwatched!

Puzzle: Figure out a system of message passing (phone calls) that enforces these restraints.
Assume there are no clocks, and you cannot predict when lunch will start or how long it will last.
What is the minimum number of messages that is required?
"""

import time
import random
import threading

from threading_cleanup import Thread


def show(name, activity):
    time.sleep(random.random() / 10)
    print(name, activity, sep=':\t', flush=True)


def work(name, lunch_break, finish):
    while not finish.is_set():
        show(name, '🛠 \tWorking')
        if random.random() < .1:
            with lunch_break:
                show(name, '🌮\tStart lunch')
                show(name, '🍉\tEnd lunch')


def main():
    lunch_break = threading.Lock()
    finish = threading.Event()
    allen = Thread(work, 'Allen', lunch_break, finish)
    bob = Thread(work, 'Bob', lunch_break, finish)
    time.sleep(.4)
    finish.set()
    
main()
