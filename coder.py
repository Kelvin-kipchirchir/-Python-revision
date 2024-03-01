#!/usr/bin/env python
print("********python functions***********")
def greetings(name,department):
	print("welcome:"+name)
	print("Mr:{}".format(name)+ "comes from{}".format(department))
greetings("Nelson","IT ")

def sum(a,b):
	print("sum is:",a+b)
sum(20,34)

def area(base,height):
	return 0.5*base*height
area_a=area(4,3)
print("the area of triange a is:{}".format(area_a))

def convert_seconds(seconds):
	hours=seconds//3600
convert_seconds(36000)

