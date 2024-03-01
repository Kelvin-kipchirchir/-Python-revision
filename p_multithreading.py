#!/usr/bin/env python
import os

print('-----------introducing multithreading---------------')
'''
Threads are lightweight process that perform certain actions in programs and they are part of a process themselves.These threads can work in parallel with each other in the same way as two individual applications can.Thread has a beginning or a start,a working sequencee and an end.But it can also be stopped or put to hold at any time.This is called sleep
Two kinds of threads Kernel threads and user threads
kernel threads are part of the operating system,whereas user threads are managed by programmer
in python,a thread is a class that can create instance of.Each of these instances then represent an individual thread that represent an individual thread which we can start,pause or stop.They are all independent from each other and they can perform different operations at the same time
in a video game,one thread could be rendering all the graphics,while another thread processes the keyboard and mouse inputs

'''
#starting threads
import threading

def hello():
    print("Hello World!!")

t1 = threading.Thread(target = hello)
t1.start()

def function1():
    for x in range (10):
        print('ONE')

def function2():
    for x in range (10):
        print('TWO')

th_1 = threading.Thread(target = function1)
th_2 = threading.Thread(target = function2)

th_1.start()#using start the output alternates between ones and twos
th_2.start()
print("this is the end of start operation")
#th_1.run()
#th_2.run()
print("this is the end of run operation and join of first thread")
th_1.join()#by using the join function here,we wait for the thread to finish before we move on to the last print statement.If we want to set a maximum time that we want to wait,we just pass the number ofseconds as a parameter
print("after join of the first thread")
print("before join the second thread")
th_2.join(5)
print("after join the second thread")

print("This is THE END")

#Thread classes
#another way to build our thread is to create a class that inherits the thread class.We can then modify the run function and implement our functionality.The start function is also using the code from the run function so we dont have to worry about that
class MyThread(threading.Thread):
    def __init__ (self,message):
        threading.Thread.__init__ (self)
        self.message = message

    def run(self):
        for x in range(10):
            print(self.message)

me_1 = MyThread('This is my thread message!')
me_1.start()

#  Synchronizing Threads
import time
x = 8192
lock = threading.Lock()#Lock is part of the threading module and we need this object in order to manage the locking.Now when we want to try to lock the resource,we use the function aquire.If the lock was already locked by someone else,we wait until it is released again before we continue with the code.However if the lock is free we lock it ourselves and release it at the end using the release function

def halve():
    global x, lock
    lock.acquire()

    while (x >1):
        x /=2
        print (x)
        print('sleeps after 2 seconds')
        time.sleep(2)
    print('END!')
    lock.release()

def double():
    global x, lock
    lock.acquire()

    while (x <16384 ):
        x *=2
        print (x)
        print('sleeps after 1 seconds')
        time.sleep(1)
    print('THE END')
    lock.release()

ts_1 = threading.Thread(target = halve)
ts_2 = threading.Thread(target = double)

ts_1.start()
ts_2.start()


#    semaphores
semaphore = threading.BoundedSemaphore(value = 5)
#we first use the BoundedSemaphore class to create our semaphore object.This parameter valuedetermines how many paralle access we allow.With our access function,we try to access the semaphore.Here,this is also done with the aquire function.If there are less than five threads utilizing the semaphore,we can acquire it and continue with the code.But whenits full,we need to wait until some other thread frees up one space.This process makes a lot of sense when we have limited resources or limited computational power in a system and we want to limit the access to it.
def access(thread_number):
    print('{}: Trying access...'.format(thread_number))
    semaphore.acquire()
    print('{}: Access granted!!'.format(thread_number))
    print('{}: Waiting 5 seconds...'.format(thread_number))
    time.sleep(5)
    semaphore.release()

    print('{}: Releasing!'.format(thread_number))

for thread_number in range(10):
    tsem = threading.Thread(target = access,args = (thread_number,))
    tsem.start()

#we first use the BoundedSemaphore class to create our semaphore object.The parameter value determines how many paralel accesses we allow.5 chosen above.With our access function,we try to access the semaphore.Here is also done with the acquire function.if there are less than 5 threads utilizing the semaphore,we can aquire it and continue with the code.But when its full,we need to  wait some other thread frees up one space.
#->when we run this code,you will see that the first five threads will immediately run the code,whereas the remaining five threads will need to wait 5 seconds until first thread release the samaphore


#   events
#with events we can manage threads better.we can pause a thread and wait for certain event to happen,in order to continue it.
event = threading.Event()
 
def function():
    print('Waiting for event....')
    event.wait()
    print('Continuing!')

e_th = threading.Thread(target = function)
e_th.start()

x = input ('Trigger event?')
if (x == 'yes'):
    event.set()

#To define an event we use the Event class of the threading module.Now we define our function which waits for our event.This is done with the wait function.So we start the thread and it waits.
#then we ask the user,Then we ask the user, if he wants to trigger the event. If the answer is yes,we trigger it by using the set function. Once the event is triggered, ourfunction no longer waits and continues with the code.

#DAEMON THREADS
'''So-called daemon threads are a special kind of thread that runs in the
background. This means that the program can be terminated even if this
thread is still running. Daemon threads are typically used for background
tasks like synchronizing, loading or cleaning up files that are not needed
anymore. We define a thread as a daemon by setting the respective
parameter in the constructor for Thread to True .'''

from os import walk
dir_path =  r"C:\Users\Kelvin Walker\Desktop\backup"
res = os.listdir(dir_path)
res = []
for (dir_path,dir_names,file_names) in walk(dir_path):
    res.extend(file_names)
print(res)

