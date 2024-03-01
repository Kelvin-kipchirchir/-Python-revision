#!/usr/bin/env python
print("-----------introducing python dictionaries--------------")
'''
used to implement key value pair in python
'''
Employee = {"Name":"kelvin kipchirchir",
        "Age":25,
        "Salary":65000,
        "Company":"KRA",
        "Designation":"SOC Analyst"}
print(type(Employee))
print("printing employee data:",Employee)
print("employee name is:{}".format(Employee["Name"]),"from:{}".format(Employee["Company"]),"Aged:{}".format(Employee["Age"]),"works as a:{}".format(Employee["Designation"]))
print("updating the dictionary list using the specific keys")
print("the original dictionary is:",Employee)
Employee["Salary"] = int(input("Please enter the new salary"))
Employee["Company"] = input("please enter the company name:")
print("Updated employee list is:",Employee)

print("------dictionary operations--------------")
option = int(input("what do you wish to delete?\n1.Name\t2.Age\t3.Company\t4.Designation\t5.clear\t6.copy\t"))
if option == 1:
    del Employee["Name"]
    print("employee name deleted successfully")
elif option == 2:
    del Employee["Age"]
    print("employee age deleted successfully")
elif option == 3:
    del Employee["Salary"]
    print("employee salary deleted successfully")
elif option == 4:
    del Employee["Designation"]
    print("employee designation deleted successfully")
elif option == 5:
    Employee.clear()
    print("you have deleted everything in the dictionary")
elif option == 6:
    Employee2 = Employee.copy()
    print("printing the components of second dictionary",Employee2)
else:
    print("have selected invalid operand")

print("Updated employee list becomes:",Employee)
print("iterating through the list:")
count = 0
for x in Employee:
    count+=1
    print(count,x)

count = 0
for x in Employee.values():
    count+=1
    print(count,x)

count = 0
for x in Employee.items():
    count+=1
    print(count,x)

print(len(Employee))
print("Current dictionary before deliting",Employee)

print("deleting age item using pop",Employee.pop("Age"))

print("dictionary after deleting items",Employee)
#print("deleting items using  popitems",Employee.popitems())
print("print updated list after deleting",Employee)
#print("doing some counting",{x:Employee.count(x) for x in Employee},"items")

print("print the index",Employee.index())
print("other dictionary functions")
#len(dict)->returns the length of a dictionaru
#str(dict)->returns the dictionary displayed as a string
#dict.clear()->removes all elements from a dictionary
#dict.copy()->returns a copy of the dictionary
#dict.fromkeys()->returns a new dictionary with the same keys but empty values
#dict.get(key)->returns the value of a given key
#dict.has_key(key)->returns if the dictionary has a certain key or not
#dict.items() ->returns all the items in a list of tuples
#dict.items() ->returns all the items in alist of tuples
#dict.keys()->returns a list of all the keys
#dict.update(dic2) ->add the content of another dictionary to an existing one
#dict.values()->returns a list of all the values

