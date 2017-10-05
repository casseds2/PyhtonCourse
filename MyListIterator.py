class MyListIterator:

	def __init__(self, MyList):
		self.my_list = MyList.my_list
		self.index = -1

	def __next__(self):
		if self.index < len(self.my_list) -1:
			index += 1
			return my_list[index]
		else:
			raise StopIteration()
