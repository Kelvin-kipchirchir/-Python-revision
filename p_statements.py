#!/usr/bin/env python
a = int(input("enter first value"))
b = int(input("enter second value:"))
c = int(input("enter third value:"))
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")

#example 2
name = input("please enter your name:")
age = int(input("enter your current age:"))
amount = int(input("enter amount of money:"))
if age>= 18 and amount >=100:
    print("you are allowed to drink")
elif age<= 18 and amount <=50:
    print("you are poor child")
elif age<18 and amount>=50:
    print("get out of here you are a child!!!")
elif age>= 18 and amount<=50:
    print("sorry you are broke")

