#!/usr/bin/env python
print("introducing the time module")
import time
import datetime
print(time.localtime(time.time()))
print("a more formatted time format:",time.asctime(time.localtime(time.time())))

#python sleep time
#sleep() method is used to stop the excecution of a script for a given amount of time
for i in range(0,5):
    print("is:",i)
time.sleep(1)

#datetime module
#enables us to create custom date objects perform various operations on dates ie comparison
#use datetime module

print(datetime.datetime.now())

#calender module
import calendar as cal
#me=dir(calendar)
#print(me)
#cal.prcal(2023)
#printing a specific month
jul = cal.month(2023,7)
print(jul)
