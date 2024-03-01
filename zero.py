#!/usr/bin/env python
print("please enter a number to check if its even odd or 0:")
number = int(input("Number:"))
if number % 2 == 0:
    if number == 0:
        print("Your number is even but Zero")
    else:
        print("Your number is even")
else:
    print("your number is odd")

