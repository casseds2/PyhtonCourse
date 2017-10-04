from __future__ import print_function
import random
import time

def myid():
	i = hex(random.randint(0, 1000000))
	print(str(i))
	#print(len(str(time.time())))	
	return str("{:0>8}".format(i)) + "-" + str(time.time())[:-5]

if __name__ == "__main__":
	print(myid())

