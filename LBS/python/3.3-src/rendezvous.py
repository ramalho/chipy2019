#!/usr/bin/env python3
 
"""
3.3 Rendezvous

Puzzle: Generalize the signal pattern so that it works both ways.
Thread A has to wait for Thread B and vice versa.

In other words, given this code...

  Thread A
 ┌────────────────
1│ statement a1
2│ statement a2

  Thread B
 ┌────────────────
1│ statement b1
2│ statement b2

...we want to guarantee that `a1` happens before `b2` and `b1` happens before `a2`.
In writing your solution, be sure to specify the names and initial values of your semaphores
(little hint there).

Your solution should not enforce too many constraints.
For example, we don’t care about the order of a1 and b1.
In your solution, either order should be possible.

This synchronization problem has a name; it’s a rendezvous.
The idea is that two threads rendezvous at a point of execution,
and neither is allowed to proceed until both have arrived.
"""

import time
import random
import threading

from threading_cleanup import Thread, Semaphore


def show(name, activity):
    time.sleep(random.random() / 10)
    print(name, activity, sep=':\t', flush=True)


def a_task(a1_action, b1_action):
    global a1_done
    show('A', f'doing a1')
    a1_done = True
    a1_action.signal()
    b1_action.wait()
    assert a1_done and b1_done
    show('A', f'doing a2')


def b_task(a1_action, b1_action):
    global b1_done
    show('B', f'doing b1')
    b1_done = True
    b1_action.signal()
    a1_action.wait()
    assert a1_done and b1_done
    show('B', f'doing b2')


a1_done = False
b1_done = False


def main():
    a1_action = Semaphore(0)
    b1_action = Semaphore(0)
    a = Thread(a_task, a1_action, b1_action)
    b = Thread(b_task, a1_action, b1_action)
    a.join()
    b.join()

    
main()
