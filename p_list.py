#!/usr/bin/env python
'''
python list->is implemented to store the sequence of various data types of data
python list usually enclosed inside a square brackets

'''
print("doing some python lists")
#items are enclosed in [] and separated by,
emp = ["john",102,"USA"]
dep1 =["cs",10]
dep2 =["IT",11]
HOD_CS = [10,"Mr Holdings"]
HOD_IT = [11,"Mr Bowen"]
print("-------printing employees data--------")
print("Name: {}".format(emp[0]),"with id:{}".format(emp[1]),"and from {}".format(emp[2]),"coutry")

print("-------printing the employees department------")
print("currently there are two departments the {}".format(dep1[0]),"with code {}".format(dep1[1]),"led by {}".format(HOD_CS[1]),"of rank {}".format(HOD_CS[0]),"and the second one is {}".format(dep2[0]),"with code {}".format(dep2[1]),"led by {}".format(HOD_IT[1]),"of rank {}".format(HOD_IT[0]))

list1 = ["kelly",100,"CS","2nd year",True]
print(list1[2])
print(list1[4])
print(list1[1:3])
print(list1[:4])

print("--------updating list values-----")
print(list1)
list1[1] = 101
print(list)
list1[3:4] = ["3rd year",False]
print(list1)
#del list1[4]
print(list1)
print("--------list operations-------")
#repetition
print(list1*2)
#concatenation
comp_list = (emp+dep1+HOD_CS)
print(comp_list)
#membership
print("Mr Bowen" in comp_list)
#iterating through the list
for i in comp_list:
    print(i)

print("printing the lenght of the list",len(comp_list))

#   adding an element to a list
li = []
n = int(input("enter the number of elements you want to put in list"))
for i in range(0,n):
    li.append(input("enter your elements here"))
    print("now printing the element")
    for i in li:
        print(i)
print(li)
print("removing some elements from the above list")
ind = input("please enter the index want to delete")
if ind in li:
    li.remove(ind)
else:
    print("value is not present")

print("printing the affected list")
for i in li:
    print(i)

print("----python built in functions------")
#     comparing lists
#print(cmp(comp_list,emp))
#    printing the length of list
print(len(comp_list))
#   appending list.append(obj)
#   clearing all elements in a list
list = [1,"one",True]
print(list)
list.clear()
print("list after clearing:",list)

# list.copy -> returning a shadow copy of the list
li_copy = li.copy()
print(li_copy)
#  list.count(obj)
print(li.count(5))
#
comp = [1,3,6,4]

print(max(comp))
print(min(comp))
#list seq

print("----------------Built in methods------------------")
print(comp_list)
print("length of the list now:",len(comp_list))
comp_list.append(100)
print("length of the list after insertion:",len(comp_list))
print(comp_list)
#list.clear
#list.copy
#list.count(obj))
#list.extend(seq)
#list.index(obj)
#list.insert(index,obj)
#list.pop(obj=list[-1])
#list.remove(obj)
me = [1,2,3,4,8,9]
print(me)
print("reversed list:",me.reverse())
print("sorting list:",me.sort())


