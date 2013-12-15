class Foo(object):

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print "someone accessed _x"
        return self._x

    @x.setter
    def x(self, value):
        print "someone modified _x"
        self._x = value

f = Foo(5)
print f.x
f.x = 7
