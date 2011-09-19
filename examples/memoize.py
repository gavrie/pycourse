
def memoize(func):
    cache = {}

    def wrapped_func(*args):
        print "before"
        if args in cache:
            result = cache[args]
        else:
            result = func(*args)
            cache[args] = result
        print "after"
        return result

    return wrapped_func

@memoize
def foo(a,b):
    print "Calculated:", a, b
    return a + b

print foo(1, 2)
print foo(1, 2)
print foo(3, 4)
print foo(1, 2)
