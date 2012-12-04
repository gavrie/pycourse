# lexical closure
def make_cached(func):
    cache = {}
    def cached_func(*key):
        if key not in cache:
            cache[key] = func(*key)
        return cache[key]

    return cached_func

# decorator

@make_cached
def calc(a, b):
    # ....
    # ...
    print "calc({}, {})".format(a,b)
    result = a + b
    return result

@make_cached
def foo(a):
    print "foo({})".format(a)
    return

def main():

    calc(3, 4)
    calc(5, 6)
    calc(3, 4)

    foo(3)
    foo(5)
    foo(3)

if __name__ == '__main__':
    main()
