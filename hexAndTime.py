from __future__ import print_function
import random
import time		

def myid():
	i = hex(random.randint(0, 0xFFFFFFFF))
	#print(str(i))
	#print(len(str(time.time())))	
	#return "{:0>8}".format(i) + "-" + str(time.time())[:-5]
	#return "{0:08X}-{1:08X}".format(str(i), int(time.time()))
	return str(i) + "-" + str(int(time.time()))

if __name__ == "__main__":
	print(myid())
