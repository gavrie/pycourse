class Counter(object):
    def __init__(self, start=0):
        self.count = start

    def incr(self):
        self.count += 1

def log_func(func):
    counter = Counter()
    def wrapped_func(*args):
        counter.incr()
        print "Before {}{} (count: {})".format(func.__name__, 
                args, counter.count)
        result = func(*args)
        print "After (return: {}) {}".format(result, func.__name__)
        return result
    return wrapped_func

@log_func
def myfunc(a):
    print "Inside myfunc"
    return a * 1000

if __name__ == '__main__':
    for i in range(3):
        print myfunc(7)
