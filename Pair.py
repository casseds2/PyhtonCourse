from __future__ import print_function

class Pair(object):
	
	'''A Class Object Representing a Pair'''

	def __init__(self, a, b):
		'''Initialize Pair With Variable a and b'''
		self.a = a
		self.b = b

	def __str__(self):
		'''String representation of class'''
		return "({0}, {1})".format(self.a, self.b) 

	def __isub__(self, other):
		'''Support for -= Opperator'''
		return Pair(self.a - other.b, self.b - other.b)

	def __sub__(self, other):
		'''Suport For - Operator'''		
		return Pair(self.a - other.b, self.b - other.b)

	def __imul__(self, other):
		'''Support for */ Opperator'''
		return Pair(self.a * other.a, self.b * other.a)

	def __mul__(self, other):
		'''Support for * Operator'''
		return Pair(self.a * other.a, self.b * other.a)
	
	def __mod__(self, other):
		'''Support for % Operator'''
		return Pair(self.a % other.a, self.b % other.b)

	def __div__(self, other):
		'''Support for / Operator'''
		return Pair(self.a / other.a, self.b / other.a)

	def getDict(self):
		'''Return the Type Dictionary'''
		return self.__dict__		


if __name__ == "__main__":
	
	##Both Pairs
	p1 = Pair(3, 3)
	p2 = Pair(2, 2)
	print(p1)
	print(p2)

	#Subtraction -=
	print(p1, "-",  p2, "=", p1-p2)

	#Multiplication *
	print(p1, "*", p2, "=", p1*p2)

	#Division /
	print(p1, "/", p2, "=", p1/p2)

	#Modulus %
	print(p1, "%", p2, "=", p1%p2)

	#Self Dictionary
	print("P1:", p1.getDict())
	print("P2:", p2.getDict())


