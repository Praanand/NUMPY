# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:19:20 2019

@author: Santosh chidura
"""
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
