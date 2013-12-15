class Foo(object):

    def __init__(self, x=None):
        self.x = x
        self.y = None

    def _bar(self):
        print "bar"
        print "self.x", self.x

    def hello(self):
        self._bar()

    def __repr__(self):
        return "<Foo whatever>"


f = Foo(777)
f.hello()
