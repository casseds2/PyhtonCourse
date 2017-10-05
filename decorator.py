from __future__ import print_function

#This is a Higher Order Function That Takes a Function Param
def make_int(f):
	def wrapper(x):
		x = int(x)
		return f(x)
	return wrapper

#Will Multiply Param by 2
@make_int
def double(x):
	return x * 2

def monitor(f):
	def wrapper(*args, **keyargs):
		print("Calling function...")
		return f(*args, **keyargs)
	return wrapper

#Will Square a Given Int
@monitor
def deco_square(x=0):
	return x * x

#@monitor is the exact same as dec_square = monitor(deco_square)

@monitor
def deco_add_five(x=5, y=0):
	return x + 5 + y

#@monitor is the exact same as dec_add_five = monitor(deco_add_five)


def add_five(x):
	return x + 5

def square(x):
	return x * x

if __name__ == "__main__":

	#print(double([1,2,3]))
	'''
	DOUBLE WORKS ON ANY SEQUENCE AS WELL AS INTEGERS
	WHAT IF WE ONLY WANT IT TO WORK WITH INTEGERS?
	WHAT IF I CANT GET AT THE FUNCTION? - USE DECORATORS
	'''

	#print(double(4.4))
	print()
	print("Decorated Square:", deco_square(4))
	print()
	print("Normal Square:", square(2))
	print()
	print("Decorated Add:", deco_add_five(y=3))
	print()
	print("Normal Add:", add_five(2))
	print()









