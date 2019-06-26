#!/usr/bin/env python3
 
"""
3.1 Signaling

Possibly the simplest use for a semaphore is signaling,
which means that one thread sends a signal to another thread to indicate that something has happened.

Signaling makes it possible to guarantee that a section of code in one thread
will run before a section of code in another thread;
in other words, it solves the serialization problem.

Assume that we have a semaphore named sem with initial value 0,
and that Threads A and B have shared access to it.

  Thread A
 ┌────────────────
1│ statement a1
2│ sem.signal()

  Thread B
 ┌────────────────
1│ sem.wait()
2│ statement b1

The word *statement* represents an arbitrary program statement.
To make the example concrete, imagine that a1 reads a line from a file,
and b1 displays the line on the screen.
The semaphore in this program guarantees that Thread A has completed a1 before Thread B begins b1.

Here’s how it works: if thread B gets to the wait statement first,
it will find the initial value, zero, and it will block.
Then when Thread A signals, Thread B proceeds.

Similarly, if Thread A gets to the signal first then the value of the semaphore will be incremented,
and when Thread B gets to the wait, it will proceed im-mediately. Either way, the order of a1 and b1 is guaranteed.

This use of semaphores is the basis of the names signal and wait,
and in this case the names are conveniently mnemonic.
Unfortunately, we will see other cases where the names are less helpful.

"""

import time
import random
import threading

from threading_cleanup import Thread, Semaphore


def show(name, activity, immediate=False):
    if not immediate:
        time.sleep(random.random() / 10)
    print(name.rjust(12), activity, sep=':\t', flush=True)


def read_task(reading):
    global line
    show('read()', '🔍\tReading line')
    line = 'Simplicity is prerequisite for reliability.'
    show('read()', '🏁\tSignal', True)
    reading.signal()


def display_task(reading):
    show('display()', '🕰\tWaiting', True)
    reading.wait()
    assert line is not None
    show('display()', f'📺\tDisplay {line!r}')

line = None

def main():
    reading = Semaphore(0)
    reader = Thread(read_task, reading)
    display = Thread(display_task, reading)
    reader.join()
    display.join()
    
main()
