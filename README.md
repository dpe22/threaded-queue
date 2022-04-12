# Project 4 - multi-threading and queueing in python

The article "Thread-Safe Synchronized Queues in Python" reviews ten different implementations of synchronous queues in python. The examples cover first in first out (FIFO), last in first out (LIFO), and priority queues (return lowest priority value first). The article also introduces how to use queues in a multithreaded environment where multiple threads will concurrently access and modify data. 

For this project, I opted to take a priority queue approach, storing the queued task and priority as a tuple. You can see in the demo screenshot below that the module correctly throws an exception after 1 second if you try to execute a task from an empty queue. One interesting problem I encountered was that the prioritization doesn't work well with multiple threads. You can see that when there are two tasks with the same priority level they both execute sequentially on the same thread. With three threads, like in this module, that should execute both priority 2 tasks on different threads at the same time, but instead it executes them sequentially on the same thread. That effectively delays one of the two high priority tasks, bumping it behind two lower priority tasks executing synchronously on other threads. I'm still trying to figure that out. 

### System Requirements
Python 3.9

### Demo
![image](https://user-images.githubusercontent.com/74585697/162864262-6d0d8f20-b3f6-40ba-a579-9d4049de8b27.png)
