# -*- encoding: utf-8 -*-
"""
Memory Usage Test using Function and List
"""
# Defining a Function
def fibonacci_fun(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Calling the Function
for n in fibonacci_fun(100000):
    print(n)

# Usage: 1,120 MB of memory
