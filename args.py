from __future__ import print_function

def argOne(a="Hello", b=" ", c="World", d="."):
	print("ArgOne: " + a+b+c+d)

def argTwo(a, b=" ", c="Blah", d="."):
	print("ArgTwo: " + a+b+c+d)

def argThree(a, *args):
	print("ArgThree: " + a + "".join(args))

def argFour(a, **keyargs):
	print("ArgFour: " + a + keyargs['b'] + keyargs['c'] + keyargs['d'])

def argFive(a, b="", c="", d=""):
	print("ArgFive: " + a+b+c+d)

def argSix(a, b, c, *arg):
	print("ArgSix: " + a+b+c+ "".join(arg))


if __name__ == "__main__":

	argOne()
	argTwo("Hello", c="World")
	argThree("Hello", " ", "World", ".")
	argFour("Hello", b=" ", c="World", d=".")
	argFive("Hello", c="World", d=".", b=" ")
	argSix("Hello", " ", "World", ".")
