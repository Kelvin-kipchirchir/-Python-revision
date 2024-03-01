#!/usr/bin/env python
print("-----------introducing modules in python------")
#python program file that contains a python code including python functions,classes and variables
#examples
#dir() function-returns a sorted list of names defined in a passed module list contains all the sub-modules variable and function defined in that module
import json
list=dir(json)
print(list)

def summation(a,b):
    return a+b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def subtraction(a,b):
    return a-b

