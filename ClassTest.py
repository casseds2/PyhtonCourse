class Animal(object):

	__name = ''
	__height = 0
	__color = ''
	__sound = ''

	def setSound(self, sound):
		self._sound = sound

	def getSound(self):
		return self.__sound

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	def setHeight(self, height):
		self.__height = height

	def getHeight(self):
		return self.__height

	def type(self):
		print 'I am an animal'

class Cat(Animal):

	__id = 'Cat'
	
	def type(self):
		print self.type(), ' which is a ' + self.__id
		

	

if __name__ == '__main__' :
	#animal = Animal()
	#animal.setName('Cat'),
	#print animal.getName()
	animal = Animal()
	cat = Cat()
	cat.type()
