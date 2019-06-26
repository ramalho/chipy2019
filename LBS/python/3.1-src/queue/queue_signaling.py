#!/usr/bin/env python3
 
"""
This is an alternative solution to the pattern in section 3.1 Signaling,
using Python's synchronized [`Queue`](https://docs.python.org/3/library/queue.html)
class.

Synchronization makes it possible to guarantee that a section of code in one thread
will run before a section of code in another thread;
in other words, it solves the serialization problem.

Assume that we have a semaphore named sem with initial value 0,
and that Threads A and B have shared access to it.

  Thread A
 ┌────────────────
1│ statement a1
2│ queue.put(data)

  Thread B
 ┌────────────────
1│ line = queue.get()
2│ statement b1

The word *statement* represents an arbitrary program statement.
To make the example concrete, imagine that a1 reads a line from a file,
and b1 displays the line on the screen.
The semaphore in this program guarantees that Thread A has completed a1 before Thread B begins b1.

Here’s how it works: if thread B gets to the `queue.get()` statement first,
the queue will be empty, and it will block.
Then when Thread A puts data on the queue, Thread B proceeds.

Similarly, if Thread A gets to `queue.put(…)` first, when Thread B gets to `queue.get()`,
it will proceed immediately. Either way, the order of a1 and b1 is guaranteed.
"""

import time
import random
import threading
import queue

from threading_cleanup import Thread, Semaphore



def show(name, activity, immediate=False):
    if not immediate:
        time.sleep(random.random() / 10)
    print(name.rjust(12), activity, sep=':\t', flush=True)


def read_task(queue):
    show('read()', '🔍\tReading line')
    line = 'Simplicity is prerequisite for reliability.'
    show('read()', '🏁\tQueueing line', True)
    queue.put(line)


def display_task(queue):
    show('display()', '🕰\tWaiting for queue', True)
    line = queue.get()
    show('display()', f'📺\tDisplay {line!r}')


def main():
    q = queue.Queue(1)
    reader = Thread(read_task, q)
    display = Thread(display_task, q)
    reader.join()
    display.join()
    
main()
