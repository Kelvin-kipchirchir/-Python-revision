#!/usr/bin/env python
'''
-----python inheritance-------
a derived class can inherit base class by just mentioning base in the bracket followed by
class can inherit multiple classes by mentioning all of them in a brackets
'''
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("animal is speaking")
class Dog(Animal):#child class dog inherits the base class animal
    def __init__(self,name):
        super(Dog,self).__init__ (name)

    def bark(self):
        print("the dog barks")
class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__ (name)

    def meaw(self):
        print("the cat meaws")
#multilevel inheritance
class Puppy(Dog):
    def eat(self):
        print("the puppy is eating a bone")

d = Dog('bosco')
c = Cat('puscat')
p = Puppy('smallpuscat')
d.speak()
d.bark()
c.speak()
c.meaw()
p.eat()
p.speak()
p.bark()

#multiple inheritance
class Calculation:
    def summation(self,a,b):
        return a+b
class Calculation2:
    def multiplication(self,a,b):
        return a*b
class Derived(Calculation,Calculation2):
    def divide(self,a,b):
        return a/b
d = Derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))

#The issubclass(sub,sup) method-used to check the relationship between specified'class
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_older(self,years):
        self.age += years

class Programmer(Person):

    def __init__(self,name,age,language):
        super(Programmer,self).__init__ (name,age)
        self.language = language

    def print_language(self):
        print("Favourite Programming Language: {}".format(self.language))

p1 = Programmer("mike",30,"Python")
print(p1.age)
print(p1.name)
print(p1.language)

p1.get_older(5)

print(p1.age)

#operator overloading
class Vector:

    def __init__ (self,x,y):
        self.x = x
        self.y = y


    def __str__ (self):
        return "X: %d,Y: %d" % (self.x,self.y)

    def __add__ (self,other):
        return Vector(self.x + other.x,self.y + other.y)

    def __sub__(self,other):
        return Vector(self.x - other.x,self.y - other.y)

#class that represents the function of a vector.When you add a vector to anothor,you need to add the individual values.We use the functions __add__ and __sub__ to define what happens when we apply the + and the - operator.The __str__ function determines what happens when we print the object
v1 = Vector(3,5)
v2 = Vector(6,2)
v3 = v1 + v2
v4 = v1 - v2
print(v1)
print(v2)
print(v3)
print(v4)

