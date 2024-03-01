#!/usr/bin/env python
print("---------------database programming----------------")
# a database that comes preconfigured with python is calledSQLite.others are MySQL,MongoDB
import sqlite3
conn = sqlite3.connect('mydata.db')# this creates the new file mydata.db and connects to this database
# Executing statements
c = conn.cursor() #in order to excecute SQL statements we need to create so called cursor
# CREATING TABLES
#c.execute("""CREATE TABLE persons (first_name TEXT,
 #       last_name TEXT,
 #      age INTEGER)""")

# INSERTING VALUES
#c.execute("""INSERT INTO persons VALUES ('john','smith',25),
#        ('ken','smith',30),
#        ('mike','tyson',40)""")

c.execute("""SELECT * FROM persons WHERE last_name = 'smith'""")
print(c.fetchall())

#simplifying work using classes and tables
class Person():

    def __init__(self,first=None,last=None,age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self,result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

        #Here we have a constructor with default parameters. In case we don’tspecify any values, they get assigned the value None . Also, we have a function clone_person that gets passed a sequence and assigns the values of it to the object. In our case, this sequence will be the tuple from the fetching results.

# FROM TABLE TO OBJECT
person = Person("julia","johnson",28)

c.execute("INSERT INTO persons VALUES (?,?,?)",(person.first,person.last,person.age))

conn.commit()
conn.close()#at the end dont forget to close the connection when you are done with everything


