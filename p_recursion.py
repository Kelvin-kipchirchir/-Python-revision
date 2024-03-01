#!/usr/bin/env python
print("-----------------welcome to python recursion---------------")
# Example of a fuctorial

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial (n-1)
        return number

factorial(5)

