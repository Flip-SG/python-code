# -*- encoding: utf-8 -*-
import time
from threading import Thread

counter = 50000000

def countdown(n):
    while n > 0:
        n -= 1


start = time.time()
countdown(counter)
end = time.time()

print(f"Time recorded in seconds: {end - start}")
# Recorded time (seconds): 7.1906898021698