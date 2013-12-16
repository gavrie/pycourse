def make_cached(func):
    cache = {}

    def cached_func(*args):
        key = args
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return cached_func

@make_cached
def calc(a, b):
    print "Running calc({}, {})".format(a, b)
    return a + b


def another_calc(a, b):
    pass

another_calc = make_cached(another_calc)




