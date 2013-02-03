from contextlib import contextmanager

@contextmanager
def mycontext():
    print "setup"
    try:
        yield
    finally:
        print "cleanup"


with mycontext():
    print "inside context"
    raise Exception('foo')
