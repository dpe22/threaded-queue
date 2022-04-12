# Code Reference: https://coderzcolumn.com/tutorials/python/queue-thread-safe-synchronized-queues-in-python
# Code Modified by dpe22

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

    thread1 = threading.Thread(target=pop_nitems, args=(3, ), name="001")
    thread2 = threading.Thread(target=pop_nitems, args=(4, ), name="002")
    thread3 = threading.Thread(target=pop_nitems, args=(5, ), name="003")

    thread1.start(), thread2.start(), thread3.start()
