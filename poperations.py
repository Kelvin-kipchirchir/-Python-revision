#!/usr/bin/env python
print("introducing python operations\n 1:addition 2:subtaction 3.division 4.multiplication 5.modulus")
a = int(input("please enter your first value:\t"))
b = int(input("please enter the second value:\t"))
print("addition is:\t",a+b)
print("subtraction is:\t",a-b)
print("division is:\t",a/b)
print("multiplication is:\t",a*b)
print("modulus is:\t",a%b)
print("exponent is:\t",a**b)
print("floor division is:\t",a//b)
print("."*100)
print("printing operand and assignment operators")
print("is a equal to b:\t",a==b)#prints true if equals else false
print("is a not equal to b:\t",a!=b)
print("is a less than or equal to b:\t",a<=b)
print("is a greater than or equal to b:\t",a>=b)
print("is a greater than b:\t",a>b)
print("is a less than b:\t",a<b)
print("."*100)
print("entering into assignment operators:\n 1.assignment(=) 2.increment(+=) 3.decrement(-=) 3.multiplier(*=) 4.divisor(%=) 5.exponent(**)")
print("assigning a into b")
print("value of a is:\t",a)
a=b
print("value of a now is:\t",a)
print("incrementing value of a")
print("value of a is:\t",a)
a+=2#incrementing by 2
print("value of a now is:\t",a)
print("decrementing value of b")
print("current value of b is:\t",b)
b-=2
print("after decrementing value of b by two:\t",b)
print("value of a is:\t",a)
a*=2
print("current value of a after multiplying by 2:\t",a)


