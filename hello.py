#!/usr/bin/env python 
import os
import random
import sys
print(sys.argv)
print("please input your name to proceed:")
name = input()
print("welcome :{}".format(name)+ "kindly provide your age to proceed")
age = int(input())
print("seems your age is :{}".format(age))
print("instructions for playing this game is easy guess any number")
rand = random.randint(0,10)#prints a random number between 0-10
for i in range(0,5):
    a = int(input("enter your number"))

    if(a <= rand):

       print("number is less try again")
    elif(a >= rand):
       print("number is greater try again")
    elif(a == rand):
       print("game over you guessed well number was: {}".format(rand))
    else:
        print("the correct answer is: {}".format(rand))
else:
    print("you have run out of options")
    print("the correct answer is: {}".format(rand))


