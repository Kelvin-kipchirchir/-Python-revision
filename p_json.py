#!/usr/bin/env python
print("introducing json is python")
import os
import sys
import json
import pandas as pd

'''
   JSON INTRODUCTION
->json is an acronym for javascript object notation,its open standard format which is lightweight and text based,designed explicitly for human-readable data formats
->it is a language-independent data format and supports almost every kind of language,framework and libary
->json is open standard for exchanging data on the web.
->it supports data structures like objects and arrays hence its easy to write and read data from json
->data is usually represented in key-value pairs,and curly braces hold objects,where colon is followed after each name.The comma is used to separate key_value pair
->square brackets are used to hold arrays,where each value is comma separated

Features of JSON
-simplicity
-opennes
-self describing
-extensibility
interoparability
 
 JSON DATA TYPES
 string-"name","1234"
 number-121
 boolean-True,False

  JSON OBJECTS
  -objects refer to dictionaries which are enclosed in curly brackets.These objects are writen in key/value pair where the key has to be a string  and values has to be a valid JSON data type such as a string,number,objects,boolean or null
  -key and values are separated by a colon,and comma separates each key/value pair

'''
#example
emp={"name":"jack","employeeid":1,"present":False}
'''
  JSON ARRAYS
  ->arrays can be understood as a list of objects,which are mainly enclosed in square brackets[].
  ->an array value can be a string,number,object,array,boolean or null

'''
j_array = [{
    "PizzaName":"county Feast",
    "Base":"cheese burst",
    "Toppings":["jalepenos","Black olives","Extra cheese","Cherry tomatoes"],
    "spicy":"yes",
    "veg":"yes"
    },
    {"PizzaName":"Veggie paradise",
        "Base":"Thin crust",
        "Toppings":["jalepenos","Black olives","Grilled mashrooms","onions"],
        "spicy":"yes",
        "veg":"yes"
        }]

print("an example of json array",j_array)

data = {
        "employee":{
            "name":"kelvin walker",
            "salary":2400,
            "married": True
            }
        }
print(data)
