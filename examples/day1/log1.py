class Counter(object):
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


def log_func(func):
    counter = Counter()
    def wrapped_func(*args):
        counter.increment()
        print "Before {} (count: {})".format(func.__name__, counter.value)
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
