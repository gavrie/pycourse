class Foo(object):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "<Foo {}>".format(self.x)

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)

f1 = Foo(100)
f2 = Foo(100)

print "f1 == f2?", f1 == f2

d = {}
d[f1] = "f1"
d[f2] = "f2"

print d
