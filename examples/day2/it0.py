class Foo(object):

    def __iter__(self):
        print "making iterator"
        return self

    def __init__(self):
        print "new iter"
        self.i = 0

    def next(self):
        if self.i < 5:
            self.i += 1
            return self.i
        else:
            print "done"
            raise StopIteration
