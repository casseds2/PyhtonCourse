class Iterator(object):
	
	def __init__(self, data):
		self.data = data
		self.index = -1

	def __iter__(self):
		return self

	def next(self):
		if self.index < len(self.data)-1:
			self.index += 1
			return self.data[self.index]
		raise StopIteration

if __name__ == "__main__":

	result = ""
	iter = Iterator(['Hello', ' ', 'World', '.'])
	for i in iter:
		result += i
	print(result)
