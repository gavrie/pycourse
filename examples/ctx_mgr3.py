from contextlib import contextmanager

class ReferenceCounterException(Exception): pass

class ReferenceCounter(object):

    def __init__(self):
        self._refcount = 0

    def addRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self.onFirstUsageStart()

    def decRef(self):
        if self._refcount == 0:
            raise ReferenceCounterException("Cannot decrease reference count below zero")
        self._refcount -= 1
        if self._refcount == 0:
            self.onLastUsageEnd()

    def onFirstUsageStart(self):
        pass

    def onLastUsageEnd(self):
        pass
    

class ContextManagedRefCounter(ReferenceCounter):
    
    def __init__(self, obj):
        super(ContextManagedRefCounter, self).__init__()
        self.obj = obj

    def __enter__(self):
        self.addRef()
        return self.obj
    
    def __exit__(self, *args):
        self.decRef()
