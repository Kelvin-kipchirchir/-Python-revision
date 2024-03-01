#!/usr/bin/env python
"LIFO QUEUES An alternative to the FIFO queues would be the LIFO queues . That stands for last in first out . You can imagine this queue like some sort of stack. The element you put last on top of the stack is the first that you can get from it."
import queue
q = queue.LifoQueue()
numbers = [1,2,3,4,5,6]
for n in numbers:
    q.put(n)

while not q.empty():
    print(q.get())
"By using the LifoQueue class from the queue module, we can create an instance of this type.When we now put in the numbers one to five in ascending order,we will get them back in descending order."

'Prioritizing Queues->Here every element gets assigned a level of priority that determines when they will leave the queue'
q1 = queue.PriorityQueue()
q1.put((8,'Some String'))
q1.put((1,2023))
q1.put((90,True))
q1.put((2,10.23))

while not q.empty():
    print(q.get())

#Here, we create a new instance of the class PriorityQueue . When we put anew element into this queue, we need to pass a tuple as a parameter. The first element of the tuple is the level of importance (the lower the number,the higher the priority) and the second element is the actual object or value that we want to put into the queue.When we execute the print statement of the loop, we get the following results:
   # (1, 2023)
   # (2, 10.23)
   # (8, 'Some string')
   # (90, True)
#    As you can see, the elements got sorted by their priority number. If you only want to access the actual value, you need to address the index one because it is the second value of the tuple.
while not q.empty():
    print(q.get()[1])
