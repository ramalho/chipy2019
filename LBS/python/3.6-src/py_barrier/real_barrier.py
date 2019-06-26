#!/usr/bin/env python3
 
"""
3.6 Barrier

Consider again the Rendezvous problem from Section 3.3.
A limitation of the solution we presented is that it does not work with more than two threads.

Puzzle: Generalize the rendezvous solution. Every thread should run the following code:

  Barrier code
 ┌────────────────
1│ rendezvous
2| critical point

The synchronization requirement is that no thread executes critical point until after all threads have executed rendezvous.
You can assume that there are n threads and that this value is stored in a variable, n, that is accessible from all threads.
When the first n − 1 threads arrive they should block until the nth thread arrives, at which point all the threads may proceed.
"""

import time
import random
import threading

from threading_cleanup import Thread, Semaphore


def show(name, activity):
    time.sleep(random.random() / 10)
    print(name, activity, flush=True)


def show_barrier():
    print(total_threads, '#' * 50, flush=True)


def work(thread_id, barrier):
    show('\t' * thread_id, f't{thread_id} 🔽')
    show('\t' * thread_id, f't{thread_id} 🔴')
    barrier.wait()
    show('\t' * thread_id, f't{thread_id} 🔷')


total_threads = 5

def main():
    barrier = threading.Barrier(total_threads, show_barrier)
    counter_lock = threading.Lock()
    threads = [Thread(work, t, barrier)
                for t in range(total_threads)]
    for thread in threads:
        thread.join()

main()