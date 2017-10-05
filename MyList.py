from __future__ import print_function 

class MyListIterator:

	def __init__(self, MyList):
		self.my_list = MyList.my_list
		self.index = -1

	def next(self):
		if self.index < len(self.my_list) -1:
			self.index += 1
			return self.my_list[self.index]
		else:
			raise StopIteration()

###################################################

class MyList(object):

	def __init__(self, li):
		self.my_list = li

	def __iter__(self):
		return MyListIterator(self)

if __name__ == "__main__":

	myList = MyList([1, 2, 3, 4, 5])
	for elem in myList:
		print(elem, end=" ")
	print()
