#!/usr/bin/env python
print("----using the p_modules.py------")
from p_modules import summation,division,multiplication
from p_modules import multiplication as mult

a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
print("sum of two numbers is:",summation(a,b))

