def log_func(func):
    counter = [0]
    def wrapped_func(*args):
        counter[0] += 1
        print ">>> Entering {}{} [call count: {}]".format(
                func.__name__, args, counter[0])
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
    print """Write a decorator, called log_func, that has adds the following
    behavior to a function that it decorates:

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
