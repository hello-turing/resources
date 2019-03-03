import threading 
import multiprocessing
import time
import random

#def worker(number):
#	sleep = random.randrange(1, 10)
#	time.sleep(sleep)
#	print("I am Worker {}, I slept for {} seconds".format(number, sleep))
#
#
#for i in range(5):
#	t = threading.Thread(target=worker, args=(i,))
#	t.start()
#
#print("All Threads are queued, let's see when they finish!")


def worker(number):
	sleep = random.randrange(1, 10)
	time.sleep(sleep)
	print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
	t = multiprocessing.Process(target=worker, args=(i,))
	t.start()

print("All Processes are queued, let's see when they finish!")