from __future__ import print_function

def fibOne(n):
	result = []
	a, b = 0, 1
	yield a
	while a < n:
		#result.append(a)
		yield b
		a, b = b, a+b
	#return result
 
def fibTwo(n):
	previous = 0
	current = 1
	yield previous
	while current < n:
		yield current
		current, previous = current+previous, current

if __name__ == "__main__":
	

	print("FibOne:", list(fibOne(100)))
		
	print("FibTwo:", list(fibTwo(100)))
