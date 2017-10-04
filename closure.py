from __future__ import print_function

def closureFunc():
	def print_string():
		print(string)
	string = "Hello World"
	return print_string

if __name__ == "__main__":
	closureFunc()()
