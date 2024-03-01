#!/usr/bin/env python
print("hello world welcome to python")
myNumber = 10
myText = "hello world"
print(myNumber)
print(myText)


a = 20
b = 30
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
elif a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("unable to distinguish any value")
name = input("Please enter your name:")
print("welcome :{}".format(name))

print("doing some calculatuins")
print ("kindly input some numbers to perform")
number1 = int(input("Enter the first value:"))
number2 = int(input("Enter the second value:"))
sum = number1 + number2
sub = number1 - number2
div = number1 / number2
mult = number1 * number2

print("sum is:{}".format(sum))
print("sub is:{}".format(sub))
print("division is:{}".format(div))
print("multiplication is:{}".format(mult))


