def make_cached(func):
    import pdb
    pdb.set_trace()

    cache = {}

    def cached_func(*key):
        if key in cache:
            return cache[key]
        result = func(*key)
        cache[key] = result
        return result

    return cached_func

@make_cached
def calc(a, b):
    # ...
    print "calc({}, {})".format(a, b)
    return 123

#######

def main():

    calc(3, 5)

    calc(4, 6)
    calc(3, 5)

main()
