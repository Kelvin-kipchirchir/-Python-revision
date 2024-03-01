#!/usr/bin/env python
import os
import time
import threading

print("==========welcome to daemon threads=========")
#DAEMON THREADS
'''So-called daemon threads are a special kind of thread that runs in thebackground. This means that the program can be terminated even if this
thread is still running. Daemon threads are typically used for backgroundtasks like synchronizing, loading or cleaning up files that are not needed
anymore. We define a thread as a daemon by setting the respective
parameter in the constructor for Thread to True .'''

from os import walk
dir_path =  r"C:\Users\Kelvin Walker\Desktop\backup"
res = os.listdir(dir_path)
res = []
for (dir_path,dir_names,file_names) in walk(dir_path):
        res.extend(file_names)
        print(res)

if 'hot.txt' in res:
    text = ''

def readFile():
    global dir_path,text
    while True:
        with open (dir_path) as file:
            text = file.read()
        time.sleep(3)

