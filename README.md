# Project 4
###### practice with multi-threading and queue systems in python

The article "Thread-Safe Synchronized Queues in Python" reviews ten different implementations of synchronous queues in python. The examples cover first in first out (FIFO), last in first out (LIFO), and priority queues (return lowest priority value first). The article also introduces how to use queues in a multithreaded environment where multiple threads will concurrently access and modify data. 

For this project, I opted to take a priority queue approach, storing the queued task and priority as a tuple. 

### System Requirements
Python 3.9
