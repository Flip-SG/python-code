# -*- encoding: utf-8 -*-
"""
Teste de Utilização de Memória com Geradores

Este teste irá comparar a utilização de memória quando executamos o mesmo programa com Funções utilizando Listas
com 100.000 valores e Geradores com 100.000 valores.

Para realizar o teste utilizaremos a sequência de Fibonacci.
A Sequência de Fibonacci consiste em uma sucessão de números, tais que, definindo os dois primeiros números da sequência
 como 0 e 1, os números seguintes serão obtidos por meio da soma dos seus dois antecessores.
Portanto, os números são: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181...
"""
# Teste de Memória
# Utilizando Funções

def fibonacci_fun(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Chamando a função
for n in fibonacci_fun(100000):
    print(n)
# Utilização: 1060 MB no Windows 10
