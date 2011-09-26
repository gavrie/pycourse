class Foo(object):

    def __init__(self):
        print "new Foo"

    def __iter__(self):
        print "making iterator"
        return FooIter()

class FooIter(object):
    def __init__(self):
        print "new FooIter"
        self.i = 0

    def next(self):
        if self.i < 5:
            self.i += 1
            return self.i
        else:
            print "done"
            raise StopIteration

