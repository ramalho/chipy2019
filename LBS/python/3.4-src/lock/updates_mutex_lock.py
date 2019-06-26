#!/usr/bin/env python3

"""
Puzzle: Suppose that 100 threads run the following program concurrently
(if you are not familiar with Python, the `for` loop runs the update 100 times.):

```python
for i in range(100):
    temp = count
    count = temp + 1
```

What is the largest possible value of count after all threads have completed?

What is the smallest possible value?

Hint: the first question is easy; the second is not.

"""

import random
import time

from threading_cleanup import Thread
from threading import Lock

def update(thread_id, updating):
    global count
    time.sleep(random.random() / 100)
    print(f'#{thread_id}', end='', flush=True)
    for i in range(100):
        updating.acquire()
        temp = count
        print('.', end='', flush=True)
        time.sleep(random.random() / 5000)
        count = temp + 1
        updating.release()

count = 0

def main():
    updating = Lock()
    threads = [Thread(update, t, updating) for t in range(100)]
    for thread in threads:
        thread.join()
    print('\ncount:', count)

main()
