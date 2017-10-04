from __future__ import print_function

class Animal(object):
	
	'''A class representing an animal'''
	
	def __init__(self, name, noise, height=0):
		'''class intializer, name set to string Animal '''
		self.name = name
		self.noise = noise
		self.height = height


	def attrbs(f):
		'''Function that will get/set a number of attributes'''		
		def wrapper(*args, **kargs):
			return f(*args, **kargs)
		return wrapper

	@attrbs
	def set_attrbs(self, name, noise, height):
		self.name = name
		self.noise = noise
		self.height = height

	@attrbs
	def get_attrbs(self):
		return self.name + " : " + self.noise + " : " + str(self.height)


	def __str__(self):
		return self.name + " : " + self.noise + " : " + str(self.height)


if __name__ == "__main__":
		
	animal_one = Animal("Lion", "Meow", 2)
	animal_two = Animal("Tiger", "Roar", 2)
	print("Animal One:", animal_one.get_attrbs())
	print("Animal Two:", animal_two.get_attrbs())
	animal_one.set_attrbs('Cat', "Hi!", 5)
	print("Animal One:", animal_one.get_attrbs())








