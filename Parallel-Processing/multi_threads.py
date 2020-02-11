# -*- encoding: utf-8 -*-
"""
This module provides low-level primitives for working with multiple threads (also called light-weight processes or
tasks) — multiple threads of control sharing their global data space. For synchronization, simple locks (also called
mutexes or binary semaphores) are provided. The threading module provides an easier to use and higher-level threading
API built on top of this module.
"""

import time
from threading import Thread

counter = 50000000

def countdown(n):
    while n > 0:
        n -= 1


t1 = Thread(target=countdown, args=(counter//2,))
t2 = Thread(target=countdown, args=(counter//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Time recorded in seconds: {end - start}")
# Recorded time (seconds): 7.672566652297974