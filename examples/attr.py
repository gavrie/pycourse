class Foo(object):
	def __init__(self, a):
		self._a = a

	@property
	def a(self):
		return self._a

	@a.setter
	def a(self, value):
		print "setter"
		self._a = value

f = Foo(123)
print f.a
f.a = 5
print f.a
