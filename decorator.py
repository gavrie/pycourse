def make_cached_func(func):
    cache = {}

    def lookup_or_calculate(a, b):
        key = (a, b)
        if key in cache:
            return cache[key]
        else:
            print "Result not found for %s, calculating" % (key,)
            result = func(a, b)
            cache[key] = result
            return result

    return lookup_or_calculate

@make_cached_func
def add(a, b):
    return a + b

if __name__ == '__main__':
    print add(3,4)
    print add(3,4)
