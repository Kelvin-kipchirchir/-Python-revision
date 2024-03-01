#!/usr/bin/env python
print("exception handling using python")
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    div =a/b
    print("a/b is {}:".format(div))
except Exception:
    print("cant divide by 0")
else:
    print("hi am in else block")
'''
1)python facilitates us to not specify the exception with except statement
2)we may declare multiple exception statements since try block may contain different types of exception
3)statements that dont throw exception should be placed in a try block
'''

#example 2
try:
    #this will throw an exception as the file does not exist
    file_prt = open("me.txt","r")
except IOError:
    print("no such file found")
else:
    print("file opened successfully")
    file_prt.close()

#declaring multiple exception-useful in cases where a try block throws multiple exceptions
#try:
    #block of code
#except <Exception1>,<Exception2>,<ExceptionN>:
    #error
#else:
    #block of code

#example
try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
else:
    print("Successfully done")

#final block-we can place the important code which must be excecuted before try statement

try:
    myfile = open("file.txt","r")
    try:
        myfile.write("hello lifes good")
    finally:
        myfile.close()
except:
    print("error")

#process of raising an exception
'''
To raise an exception,raise statement is used.The exception class name follows it
an exception can be provided with the value
to access raise as keyword is used
'''
try:
    age = int(input("Enter your age:"))
    if age<18:
        raise ValueError
    else:
        print("age is valid")
except ValueError:
    print("age is not valid")

#example2
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    if b is 0:
        raise ArithmeticError
    else:
        print("dividing a and b: {}".format(a/b))
except ArithmeticError:
    print("Value of b cannot be 0")


#custom exception
class Errorincode(Exception):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return repr(self.data)

try:
    raise Errorincode(2000)
except Errorincode as ae:
    print("received error : ",ae.data)


#example of custom exceptions
try:
    print(10/0)
    text = "Hello"
    number = int(text)
except ValueError:
    print("code for ValueError....")
except ZeroDivisionError:
    print("code for ZDE")
except:
    print("Code for other exceptiond....")

#else statements
try:
    print(10/0)
except:
    print("Error!!!")
else:
    print("Everything OK!!!")

#finally statements->we have some code that shall be excecuted at the end no matter what happened,we can write it into a finally block.This code will always be excecuted even if an exception remains unhandled

try:
    print(10/0)
except:
    print("Error!")
finally:
    print("always excecuted")


