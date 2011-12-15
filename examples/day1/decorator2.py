def make_cached(func):
    cache = {}

    def cached_func(*args):
        key = args
        if key in cache:
            return cache[key]
        value = func(*args)
        cache[key] = value
        return value

    return cached_func


@make_cached
def calc(a, b):
    print "Calculating {} + {}".format(a, b)
    return a + b


if __name__ == '__main__':
    print calc(3, 4)
    print calc(5, 6)
    print calc(3, 4) # don't do again
