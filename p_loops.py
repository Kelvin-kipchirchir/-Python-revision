#!/usr/bin/env python
print("python loops:\n 1.while loop 2.do while loop 3.for loops 4.break 5.continue 6.Endless loop ")
print("printing while loop")
i= 0
while i<10:
    print("printing i:\t",i)
    i+=1

print("printing multiplication table\n")
i = 1
number = 0
number = int(input("enter the number:\n"))
while i<10:
    print("%d*%d = %d\t"%(number,i,number*i))
    i+=1


print("."*100)
print("for loop")
i=1
n=int(input("enter number to point you wish"))
for i in range(0,n):
    print(i,end='')
print("an example of a for loop multiplication table:\n")
i=1
num=int(input("enter a number to create:\t"))
for i in range(0,11):
    print("%d*%d = %d\t"%(num,i,num*i))

print("an example of a nested loop\n")
print("this will display a star pattern")
row = int(input("enter the number of rows you want to print:\t"))
i,j = 0,0
for i in range(0,row):
    print()
    for j in range(0,i+1):
        print("*",end ="")

print("."*100)
print("printing a break and continue statements")
for i in range(0,10):
    print(i)
    break
else:
    print("for loop is exhausted")

i = 1
while i<=5:
    print(i)
    i+=1
    if(i==3):
        break
    else:
        print("end of loop")

print("example of a continue statement")
for i in range(0,10):
    print(i)
    if(i==8):
        continue
    else:
        print("end of road")

list1 = [1,2,3,4,5]
count = 1
for i in list1:
    if i == 4:
        print("item has matched")
        count = count+1
        break
        print("found at ",count,"location")

print("range functions")
for x in range(1,10):
    print(x)

print("an example of a break statement:")
numb = 0
while numb <10:
    numb +=1
    if numb == 5:
        break
    print(numb)


print("an example of a continue ststement")
#tip always increase the number by one then print the valuep
number = 0
while number <10:
    number += 1
    if number == 5:
        continue
    print(number)

print("an example of a pass statement")
#pass statement is a very special statement since it does absolutely nothing
if number == 10:
    pass
else:
    pass



