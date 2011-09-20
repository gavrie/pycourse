import sys
from contextlib import contextmanager

@contextmanager
def my_manager():

    print "initialized"
    print "before"
    
    yield "something"
    
    print "exited"

if __name__ == "__main__":
    
    mgr = my_manager()
    with mgr as obj:
        print obj
