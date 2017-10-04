from __future__ import print_function

#This is a Higher Order Function That Takes a Function Param
def make_int(f):
	def wrapper(x):
		x = int(x)
		return f(x)
	return wrapper

@make_int
def double(x):
	return x * 2

if __name__ == "__main__":

	#print(double([1,2,3]))
	'''
	DOUBLE WORKS ON ANY SEQUENCE AS WELL AS INTEGERS
	WHAT IF WE ONLY WANT IT TO WORK WITH INTGERS?
	WHAT IF I CANT GET AT THE FUNCTION? - USE DECORATORS
	'''

	print(double(4.4))
