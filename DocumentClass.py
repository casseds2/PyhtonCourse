class Hello(object):
	'''A class which provides a method printing Hello World'''
	def __init__(self):
		'''Init storage for Hello World String'''
		self.string = "Hello World"

	def method(self):
		'''Prints Stored Hello World'''
		print self.string
