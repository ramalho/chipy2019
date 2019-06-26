# The Little Book of Semaphores

This directory contains examples, exercises, and experiments based on Allen Downey's
[The Little Book of Semaphores](https://greenteapress.com/wp/semaphores/).


## Semaphore method names

Below are some semaphore method names mentioned by Prof. Downey in section 2.2;
the names of the methods in the `Semaphore` classes in
[Python](https://docs.python.org/3/library/threading.html#semaphore-objects) and
[Java](https://docs.oracle.com/javase/10/docs/api/java/util/concurrent/Semaphore.html);
and the corresponding [POSIX semaphore](https://linux.die.net/man/7/sem_overview) functions.
    
| Dykstra | action      | used for | Python/Java | POSIX      | meaning
| ------- | ----------- | -------- | ----------- | ---------- | ------------
| **P**   | `decrement` | `wait`   | `acquire`   | `sem_wait` | decrement and block if the result is negative
| **V**   | `increment` | `signal` | `release`   | `sem_post` | increment and wake a waiting process if any

Prof. Downey adopted the names `wait` and `signal`.

I prefer `acquire` and `release`, which are consistent with similar methods in the `Lock` class.
