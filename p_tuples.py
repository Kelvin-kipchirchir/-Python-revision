#!/usr/bin/env python
'''
python tuples
used to store a sequence of immutable python objects similar to list since the value of items stored in a list can be changed whereas tupples cannnot
'''
print("----------------introduction to python tuples------------------")
T1 = ("kelvin",25,"ICT")
T2 =("Ken",45,"ICT")
print(T1,T2)
T3 = tuple(input("input numbers only:"))
count = 0
for i in T3:
    print("T3[%d]=%s"%(count,i))

#Tuple indexing and splitting
#similar to list by starting with 0 and ending with -1 where items are accessed through sliced operator
Tuple = (0,1,2,3,4,5)
print("printing whole tuple",Tuple)
print("print the value of index two:",Tuple[2])
print("print from the third index:",Tuple[3:])
print("print from index 2-4:",Tuple[2:4])
print("print from index 1-3:",Tuple[1:3])
print("print all numbers before four:",Tuple[:4])
#unlike lists tuple items cannot be deleted using the del keyword since they are immutable
print("-------basic tuple operations--------")
#repetition
print(Tuple*2)
#concatenation
print(Tuple +T1)
#membership
print("is 2 in T2:",2 in T2)
print("is kelvin in:","kelvin"in T1)
#iteration
for i in Tuple:
    print(i)

#len
print(len(Tuple))
print("-----------tuple inbuilt functions------------------")
#cmp(T1,T2)
print(max(T3))
print(min(T3))
'''
list vs tuple
using tuple instead of list gives us a clear idea that tuple data is constant and must not be changed
2)Tuples can simulate dictionaries without keys:[
(101,"john",22),(102,"mike",34)]
3)Tuples can be used as key inside dictionaries due to its immutable nature

while lists start with [] tuples begin with ()
while lists are mutable tuples are immutable
while lists have variable length tuples have a fixed length
while lists provide more functionality than tuples,tuple have less functionality

we can store list inside tuple or tuple inside list
'''
Employees = [(101,"Ayush",22),(102,"john",29)]
print("----printing list---------")
for i in Employees:
    print(i)
Employees[0] = (100,"David",23)
print("-----printing list after modification--------")
for i in Employees:
    print(i)


