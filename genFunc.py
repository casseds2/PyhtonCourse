from __future__ import print_function

def genFunc(x):
	for num in xrange(x):
		yield num

def flatten(x):
	for outer_elem in x:
		if isinstance(outer_elem, int):
			yield outer_elem
		else:
			for inner in outer_elem:
				yield inner


if __name__ == "__main__":

	#iterable = genFunc(5)
	#for num in iterable:
	#	print(num)

	my_tuple = ((0, (5, (6, 6))), (1,1), (2,2), (3,3))
	data = flatten(my_tuple)
	for elem in data:
		print(elem)
