# Code Reference: https://coderzcolumn.com/tutorials/python/queue-thread-safe-synchronized-queues-in-python
# Code Modified by dpe22

import threading
import queue
import time
import random


priority_queue = queue.PriorityQueue()

def pop_nitems(n):
    for i in range(n):
        time.sleep(2)
        item = priority_queue.get()
        print("Thread : {}. Retrieved & Proccessed Item : {}".format(threading.current_thread().name, item))
        #print("Thread {}. Processed Item : {}".format(threading.current_thread().name, item))
        priority_queue.task_done()


if __name__ == "__main__":

    for i in range(1, 13):
        priority_queue.put((random.randint(1, 51), "Task-{}".format(i)))

    thread1 = threading.Thread(target=pop_nitems, args=(3, ), name="P3I")
    thread2 = threading.Thread(target=pop_nitems, args=(4, ), name="P4I")
    thread3 = threading.Thread(target=pop_nitems, args=(5, ), name="P5I")

    thread1.start(), thread2.start(), thread3.start()

    priority_queue.join()

    print("\nAll items in queue completed. Exited from Main Thread\n")
OUTPUT

Thread : P3I. Retrieved & Proccessed Item : (2, 'Task-3')
Thread : P4I. Retrieved & Proccessed Item : (3, 'Task-11')
Thread : P5I. Retrieved & Proccessed Item : (3, 'Task-4')
Thread : P3I. Retrieved & Proccessed Item : (6, 'Task-10')
Thread : P4I. Retrieved & Proccessed Item : (17, 'Task-6')
Thread : P5I. Retrieved & Proccessed Item : (22, 'Task-5')
Thread : P3I. Retrieved & Proccessed Item : (24, 'Task-7')
Thread : P4I. Retrieved & Proccessed Item : (37, 'Task-8')
Thread : P5I. Retrieved & Proccessed Item : (43, 'Task-12')
Thread : P5I. Retrieved & Proccessed Item : (44, 'Task-2')
Thread : P4I. Retrieved & Proccessed Item : (46, 'Task-9')
Thread : P5I. Retrieved & Proccessed Item : (49, 'Task-1')

All items in queue completed. Exited from Main Thread
Example 9
Our ninth example is an exact copy of our third example with few minor changes. We are using PriorityQueue in this example and we are putting two tuple values in the queue as an item where the first value in the tuple is a random number in the range 1-50 and the second value is the actual value.

queue_example_9.py
import threading
import queue
import time
import random

priority_queue = queue.PriorityQueue()

def pop_nitems(n):
    for i in range(n):
        try:
            item = priority_queue.get(timeout=1)
            time.sleep(2)
            print("Thread : {}. Retrieved & Processed Item : {}".format(threading.current_thread().name, item))
            #print("Thread {}. Processed Item : {}".format(threading.current_thread().name, item))
            priority_queue.task_done()
        except Exception as e:
            print("Thread : {}. Error : {}. Queue Size : {}".format(threading.current_thread().name, type(e).__name__, priority_queue.qsize()))

def push_item(value):
    try:
        time.sleep(2)
        priority_queue.put(value, timeout=1)
        print("Put Item : {}. Queue Size : {}".format(value, priority_queue.qsize()))
    except Exception as e:
        print("Thread : {}. Error : {}. Failed to add value ({}) to queue. Queue Size : {}".format(threading.current_thread().name, type(e).__name__, value, lifo_queue.qsize()))



if __name__ == "__main__":

    for i in range(1, 21):
        t = threading.Thread(target=push_item, args=((random.randint(1, 51), "Task-{}".format(i)), ), name="PutItem-%d"%i)
        t.start()

    thread1 = threading.Thread(target=pop_nitems, args=(3, ), name="P3I")
    thread2 = threading.Thread(target=pop_nitems, args=(4, ), name="P4I")
    thread3 = threading.Thread(target=pop_nitems, args=(5, ), name="P5I")

    thread1.start(), thread2.start(), thread3.start()
    
    priority_queue.join()

    print("\nAll items in queue completed. Exited from Main Thread\n")
