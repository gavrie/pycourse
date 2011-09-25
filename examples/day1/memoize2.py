def memoize(func):
	cache = {}

	def memoized_func(*key):
		if key in cache:
			print "Found in cache: {}".format(key)
			return cache[key]
		else:
			result = func(*key)
			cache[key] = result
			return result

	return memoized_func

@memoize
def calculate(a, b):
	print "calculate({}, {})".format(a, b)
	result = a + b
	return result

@memoize
def foobar(a, b, c):
	print "foobar {} {} {}".format(a,b,c)
	return a*b*c

calculate(2,3)
calculate(3,4)
calculate(2,3)
calculate(3,4)
foobar(1,2,3)
foobar(1,2,3)
foobar(1,2,3)
