from __future__ import print_function

def genFunc(x):
	for num in xrange(x):
		yield num

#My Fucntion
def flatten(x):
	for outer_elem in x:
		if isinstance(outer_elem, tuple):
			for inner in outer_elem:
				if isinstance(inner, tuple):
					for t in flatten(inner):
						yield t
				else:
					yield inner
		else:
			yield outer_elem

#Function Unpacks Anything
def flat(x):
	for sub in x:
		try:
			for val in flatten(sub):
				yield val

		except TypeError:
			yield val
	
if __name__ == "__main__":

	#iterable = genFunc(5)
	#for num in iterable:
	#	print(num)

	my_tuple = ([100, 101,102], (1, (2, (3, 4))), (5,6), (7,8), (9,(10, (11, 12))))
	#data = flatten(my_tuple)
	#for elem in data:
	#	print(elem)

	data = flat(my_tuple)
	for elem in data:
		print(elem)
