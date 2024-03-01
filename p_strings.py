#!/usr/bin/env python
print("intoducing strings in python")
str = "hello"
my_name,age ="kevin kipchirchir",25
text = "i love you and you love me"
names = ["Alice","Bob","Carol"]
print(str)
print(str[0])#prints h
print(str[4])#prints o
print(str[:])#should print the whole string
print(str[2:])#should print llo kelvin
print(str[:3])#should print hel
print(str[0:3])#should print
print(str[1:4])
print(str[-1])

print(str*2)
print(str+my_name)
print('l' in str)#prints true
print('j' in str)#prints false
print('m' not in str)#prints true
print(str.capitalize())
print(str.casefold())
print(str.lower())
print(str.title())
print(str.swapcase())

print(text.find('you'))#finds the first occurence of a certain string
print(text.count('you'))#counts how many occurence->2

sep = '-'
print(sep.join(names))#joins a sequence to a string and separate each elementsby this particular string
text = text.replace('you','john')
print(text)

name_list = my_name.split(",")
#print(str.center(width,fillchar))
print(len(str))

for name in my_name:
    print(name)
print('my name is {} and i am {} years old'.format(my_name,age))


