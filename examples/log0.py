class Counter(object):
    """
    This is my counter.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        self._value = 0

    def increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value


def log_func(func):
    counter = Counter()
    def wrapped_func(*args):
        counter.increment()
        print ">>> Entering {}{} [call count: {}]".format(
                func.__name__, args, counter.value)
        result = func(*args)
        print "<<< Exiting {}{} => {}".format(
                func.__name__, args, result)
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
    print """Write a decorator, called log_func, that
    adds the following behavior to a function that it
    decorates:

    Usage:

    @log_func
    def myfunc(a, b):
        print "Inside myfunc"
        return a * b

    Behavior:

    """
    myfunc(3, 4)
    foo()
    myfunc(5, 6)
    foo()



