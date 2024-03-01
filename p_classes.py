#!/usr/bin/env python
print("-----python classes-------")
'''
class is a virtual entity and can be seen as a blue print of object.classes come to existance when it is instanciated
object is an istance of a class
a class contains a statement suite including fields,constructor

eg.below class Employee which contains two fields Employee ID and name,
class contains function display() used to display info of employee
self is used as a reference variable which refers to current class object.Always the first argument in the function dfn
class needs to be instansiated if we want to use the class attribute in another class ie method
-class can be instanciated by calling class using classname
'''
class Employee:
    def __init__(self,id,name):
        print("this is a parameterized constructor")
        self.name = name
        self.id = id
    def display(self):
        print("Employee name is: {}".format(self.name),"and his id is: {}".format(self.id))
    def show(self):
        print("hello",self.name)
    
emp =Employee(10,"john")
emp.display()
emp.show()

class Farmer:
    def __init__(self):
        print("example of non parameterized constructor")
    def show(self,name):
        print("Hello:",name)
fam = Farmer()
fam.show("john koel")

#Constructor->special type of method(function) which is used to initate the instance members of the class can be parameterized or non-parameterized method __init__ simulates the constructor of the class ->mostly used to initialize the class attribute
class Student:
    count = 0
    def __init__(self,name,id,room):
        Student.count = Student.count+1
        self.id = id
        self.name = name
        self.room = room
    def display(self):
        print("student's name is: {}".format(self.name),"id is: {}".format(self.id),"and dwells in room:{}".format(self.room))
s1 = Student("kelvin",101,"elgon")
s2 = Student("kipchirchir",102,"Tana")

s1.display()
s2.display()
print("the current number of students are:",Student.count)
#printing the attribute name of the object
print(getattr(s1,"name"))
#resetting the attribute  of s1 to 105
setattr(s1,"room","kilimanjaro")
#has attr->prints true if the student contains attribute with the name id
print(hasattr(s1,"marks"))
#delattr-deletes certain attributes
#delattr(s1,"room")
s1.display()
s2.display()

#built in class attribute
'''
1)__dict__ ->provides the dictionary containing the info about class namespace
2)__doc__ ->contains a string which has class documentation
3)__module__->used to access module which class is obtained
4)__name__ ->used to access class name
5)__bases__ ->contains tuple
'''
print(s1.__dict__)
print(s1.__doc__)
print(s1.__module__)
#print(s1.__name__)
#print(s1.__bases__)

class Car:
    amount_cars = 0

    def __init__(self,maker,model,hp):#the constructor
        self.maker = maker
        self.model = model
        self.hp = hp
        Car.amount_cars +=1

    def print_info(self):
        print('maker: {},model :{},HP :{}'.format(self.maker,self.model,self.hp))
        #function prints out info about the respective object
    def print_car_amount(self):#another constructor
        print("Amount: {}".format(Car.amount_cars))
    
    def __del__(self):#destructor function
        print('Object gets deleted!!')#we print an information message and decrease the amount of existing car by one each time an object gets deleted
        Car.amount_cars -=1

car1 = Car("Honda","Honda",2400)
car2 = Car("Mustang","Subaru",34555)
car3 = Car("BMW","X3",2000)
car4 = Car("Porsche","911",3555)
car1.print_info()
car2.print_info()
car2.print_car_amount()
print(car1.hp,car2.hp)

del car3
car1.print_car_amount()

#hidden attributes->if you want to create hidden attributes that can only be accessed within the class
class MyClass:
    def __init__(self):
        self.__hidden = "Hello"
        print(self.__hidden)#works

m1 = MyClass() 
print(m1.__hidden)#does not work
#by putting two underlines before the attribute name,we make it invisible from outside the class,The first print works because its inside of class


