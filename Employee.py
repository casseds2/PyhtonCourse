from __future__ import print_function

class Employee(object):
	
	def __init__(self, name="Unknown", stat="Unemployed", wage = 0):
		self.stat = stat
		self.name = name
		self.wage = wage

	def __str__(self):
		return self.name + " is: " + self.stat

	@staticmethod
	def calcTax(x):
		return float(x) * 0.25

	@property
	def status(self):
		return self.stat
	@status.setter
	def status(self, stat):
		self.stat = stat

	@property
	def title(self):
		return self.name
	@title.setter
	def title(self, name):
		self.name = name

if __name__ == "__main__":

	empOne = Employee("David", "Employed", 100000)
	empTwo = Employee(wage = 20000)
	print(empOne)
	print(empTwo)
	empOne.status = "Unemployed"
	print(empOne)
	empTwo.status = "Employed"
	empTwo.title = "Stephen"
	print(empTwo)
	print(empOne, "and tax:", empOne.calcTax(empOne.wage))
	print(empTwo,  "and tax:", empOne.calcTax(empTwo.wage))
	#print(emp.calcTax(50000))
