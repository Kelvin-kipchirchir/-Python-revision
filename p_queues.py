#!/usr/bin/env python
print('--------welcome to python queues-----------')
'queues are structures that take in data in certain order to then output it in certain order.The default queue type is the so-called FIFO Queue.The elements that enter the queue first are also the elements that will leave the queue first'
'In order to work with queues in python we need to import the module queue.we can then create an instance of class queue'
import os
import queue
import threading
import math

q = queue.Queue()
for x in range(5):
    q.put(x)#we put in the numbers one to five into our queue.Then we just get the elements and print them.The order stays the same since the default queue is FIFO

for x in range(5):
    print(q.get(x))

#in above using two functions here -put and get.put function adds an element to the queue that can be extracted by the get function.

"QUEUING RESOURCES Let’s say we have a list of numbers that need to be processed. We decide to use multiple threads, in order to speed up the process. But there might be a problem. The threads don’t know which number has already been processed and they might do the same work twice, which would be unnecessary. Also,solving the problem with a counter variable won’t always work, because too many threads access the same variable and numbers might get skipped.In this case we can just use queues to solve our problems. We fill uour queue with the numbers and every thread just uses the get function, to get the next number and process it.Let’s say we have the following worker function:"

q1 = queue.Queue()
threads = []

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))

q.task_done() 
"We start out with an empty queue and an empty list for threads.Our function has an endless loop that gets numbers from the list and calculates the factorial of them. For this factorial function, we need to import the module math.But you can ignore this part, since it is only used because the computation requires a lot of resources and takes time. At the end, we use the function task_done of the queue, in order to signal that the element was processed."

for x in range(5):
    t = threading.Thread (target = worker)
    t.start()
    threads.append(t)

sahlen = [120,14,300,98,11,22]

for item in sahlen:
    q.put(item)

q.join()

for i in range(5):
    q.put(None)


"We then use a for loop to create and start five threads that we als add to our list.After that, we create a list of numbers, which we then all put into the queue."
"The method join of the queue waits for all elements to be extracted and processed. Basically, it waits for all the task_done functions. After that, we put None elements into the queue, so that our loops break.Notice that our threads can’t process the same element twice or even skip one because they can only get them by using the get function.If we would use a counter for this task, two threads might increase it at the same time and then skip an element. Or they could just access the same element simultaneously. Queues are irreplaceable for tasks like this. We will see a quite powerful application of queues in the chapter about networking ."

