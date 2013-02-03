def log_func(func):
    counter = 0
    def wrapped_func(*args):
        counter = counter + 1
        print ">>> Enter {}{} (count: {})".format(
                func.__name__, args, counter)
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
