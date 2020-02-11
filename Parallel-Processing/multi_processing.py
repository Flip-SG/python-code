# -*- encoding: utf-8 -*-
"""
multiprocessing is a package that supports spawning processes using an API similar to the threading module.
The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter
Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully
leverage multiple processors on a given machine. It runs on both Unix and Windows.

The multiprocessing module also introduces APIs which do not have analogs in the threading module. A prime example of
this is the Pool object which offers a convenient means of parallelizing the execution of a function across multiple
input values, distributing the input data across processes (data parallelism)
"""

import time
from multiprocessing import Pool

counter = 50000000

def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [counter//2])
    r2 = pool.apply_async(countdown, [counter // 2])
    pool.close()
    pool.join()
    end = time.time()
    print(f"Time recorded in seconds: {end - start}")
    # Recorded time (seconds): 4.079596042633057