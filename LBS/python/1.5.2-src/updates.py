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

def update():
    global count
    # time.sleep(random.random() / 10)
    for _ in range(100):
        temp = count
        time.sleep(0)
        count = temp + 1

count = 0

def main():
    threads = [Thread(update) for t in range(100)]
    for thread in threads:
        thread.join()
    print('count:', count)

main()
