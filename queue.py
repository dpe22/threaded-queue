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
