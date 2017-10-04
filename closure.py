from __future__ import print_function

def closureFuncOne():
	def print_string():
		print(string)
	string = "Hello World One"
	return print_string

def closureFuncTwo():
	def print_string_one():
		def print_string_two():
			print(stringTwo)
		stringTwo = "World Two"
		print(stringOne, end=" ")
		return print_string_two
	stringOne = "Hello"
	return print_string_one

def closureFuncThree():
	def print_string_one():
		def print_string_two():
			def print_string_three():
				print(stringThree)
			stringThree = "Three"
			print(stringTwo, end = " ")
			return print_string_three
		stringTwo = "World"
		print(stringOne, end=" ")
		return print_string_two
	stringOne = "Hello"
	return print_string_one

def outer(x):
	def middle(y):
		def inner(z):
			print(x,y,z,a,b)
		b = "functions"
		return inner
	a = "order"
	return middle

if __name__ == "__main__":
	closureFuncOne()()
	closureFuncTwo()()()
	closureFuncThree()()()()
	outer("Welcome")("To")("Higher")

'''

NOTE HOW STRING IS CARRIED WITH THE print_string() FUNCTION.
THIS IS INBUILT FUNCTIONALITY WITH PYTHON WHERE IT WILL TAKE THE STRING

'''
