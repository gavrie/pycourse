def log_func(func):
    counter = [0]
    def wrapped_func(*args):
        counter[0] = counter[0] + 1
        print "Before {} (count: {})".format(func.__name__, counter[0])
        result = func(*args)
        print "After {}".format(func.__name__)
        return result
    return wrapped_func

@log_func
def myfunc(a):
    print "Inside myfunc"
    return a * 1000

if __name__ == '__main__':
    for i in range(3):
        print myfunc(7)
