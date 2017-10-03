from __future__ import print_function

__author__ = "Stephen Cassedy"
__version__ = "1.0.0"
__date__ = "3/10/17"

def change(params):
	my_list = params.split(' ')
	x = []
	for w in xrange(0, len(my_list), 2):
		x.append(my_list[w])
		#my_list.remove(my_list[w])
		#print(my_list)
	return x

if __name__ == "__main__":
	words = "This mostly is some text which I would want now to quickly simplify"
	print((' '.join(change(words))).upper())
