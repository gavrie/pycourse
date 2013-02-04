class Counter(object):
    def __init__(self, start=0):
        self._count = start

    def increment(self):
        self._count += 1

    @property
    def count(self):
        return self._count

def log_func(func):
    counter = Counter()
    def wrapped_func(*args):
        counter.increment()
        print ">>> Enter {}{} (count: {})".format(
                func.__name__, args, counter.count)
        result = func(*args)
        print "<<< Exit {} [return: {}]".format(
                func.__name__, result)
        print
        return result
    return wrapped_func

@log_func
def foo():
    print "Inside foo"

@log_func
def myfunc(a, b):
    print "Inside myfunc"
    return a * b

if __name__ == '__main__':
    myfunc(3, 4)
    foo()
    myfunc(5, 6)
    foo()
