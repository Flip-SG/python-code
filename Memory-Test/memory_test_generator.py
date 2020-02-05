# -*- encoding: utf-8 -*-
""""
Memory Usage Test using Generator
"""
# Defining a Generator
def fibonacci_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Calling the Generator
for n in fibonacci_gen(100000):
    print(n)

# Usage: 690 MB of memory