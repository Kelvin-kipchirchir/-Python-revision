#!/usr/bin/env python 
#functions are organized block of reusable code which can be calledwhenever required
print("----------------intoducing python functions----------------")
#print non-parameterized function
def hello_world():
    print("jambo this is kenya")
hello_world()

#parameterized function
def func(name):
    print("hi",name)
name = input("Please enter your name to complete:")

#functions with default parameters
def say(text = "Default Text"):
    print(text)


def print_sum(*numbers):
    result = 0
    for x in numbers:
        result += x
    print(result)
print_sum(10,20,20,30)



#function to calculate the sum
def sum(a,b,c):
    return a+b+c

a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
c = int(input("Enter the third value:"))
print("sum is:",sum(b,a,c))

#call by reference
#in python all functions are calle by reference ie the changes made to the reference inside function reset back to original value
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function=",list1)
    #defining the list
list1 = [10,40,50]
    #calling the function
change_list(list1) 
print("list outside function=",list1)


def change_string(str):
    str = str + "love you"
    print("printing the string inside function:",str)
new_str = "Hi am here"
#calling a function
change_string(new_str)
print("printing the string outside function:",new_str)


#types of arguments
#1.required arguments->are arguments which are required to be passed at the time of function calling within the exact match of their position in the functionless calls and function definition an example
def fun(name):
    message = "hi"+name
    return message
name=input("enter your name:")
print(fun(name))

def simple_interest(p,r,t):
    return(p*r*t)/100
p=float(input("Enter the principle:"))
r=float(input("Enter the rate:"))
t=float(input("Enter the time:"))
print("simple interest becomes:",simple_interest(p,r,t))
 #keyword arguments->kind of functional call will enable us to pass the argument in a random order
def calling(name,message):
     print("hello:",name,"here is your message:",message)
calling(message="come home imediatelly",name="kelvin")

#example2
def simp_interest(p,r,t):
    return(p*r*t)/100
print("simple interest is:",simp_interest(p=20000,r=10,t=4))

#default arguments
#python allows us to initialize the arguments of the function obj if the value of any of the argument is not provided at the time of function then that argument can be initiated within the value given in definition
def print_me(name,age=22):
    print("my name is",name,"and age is:",age)
print_me(name="john")

#variable length argument
#in large projects sometimes we may not know the no of arguments to be passed in advance;python provides us with the flexibility to provide some 
def printme(*names):
    print("type of passed argument is",type(names))
    print("printing the passed argument")
    for name in names:
        print(name)
printme("john","james","peter","judas")


#scope of variable 
#can be either global or local-global defined an accessed outside a function while local declared an only accessed within that function
def print_message():
    message ="i am going to print a message"
    print(message)
print_message()
#print(message)#will cause an error since you are trying to access it outside

def calculate(*args):
    sum = 0
    for arg in args:
        sum = sum+arg
    print("the sum is:",sum)
    sum = 0
calculate(10,20,30)
print("values of the sum outside the function:",sum)
'''
python lambda function
python allows us not to declare the function in a standard manner ie by using def keyword rather anonymous func declared using lamda keyword
lambda accepts any number of arguments but returns only a form of exp

main role of lambda function is when we want to use them anonymous inside another function
'''
#example
x=lambda a:a+10  # a is an argument and a+10 is an expression which got evaluated and returned
print("sum=",x(20))
x=lambda a,b:a+b
print("sum=",x(20,10))

#following function prints table(n)
def table(n):
    return lambda a:a*n #a will contain the iteration variable and a multiply of n is returned as each func call
n=int(input("Enter the number:"))
b = table(n)#the entered number is passed into the func table .b will contain lambda function which will be called again and again
for i in range(1,11):
    print(n,"x",i,"=",b(i)) #the lambda function b is called with the iteraion var 1

#a lambda function that filters out a list which contains odd numbers
list = [1,3,4,5,122,239]
#oddlist = list(filter(lambda x:x%3==0,list))# the list contains all the items of the list for which the lambda functionevaluates to true
#print(oddlist)

#program to tripple each of the list value
list_p = (1,2,3,4,5)
new_list = list_p(map(lambda x:x*3,list_p))#returns tripple of each item on list
print(new_list)



