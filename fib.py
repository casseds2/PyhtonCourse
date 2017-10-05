from __future__ import print_function

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fibThree(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibThree(n-1) + fibThree(n-2)

def fibOne(n):
	result = []
	a, b = 0, 1
	yield a
	while a < n:
		#result.append(a)
		yield b
		a, b = b, a+b
	#return result
 
def fibTwo(n):
	previous = 0
	current = 1
	yield previous
	while current < n:
		yield current
		current, previous = current+previous, current

if __name__ == "__main__":
	

	print("FibOne:", list(fibOne(100)))
		
	print("FibTwo:", list(fibTwo(100)))

	memoRes = memoize(fibThree)(30)
	print("FibThree:", memoRes)
