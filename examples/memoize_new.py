def make_cached(func):

    cache = {}

    def cached_func(*key):
        if key not in cache:
            cache[key] = func(*key)
        return cache[key]

    return cached_func

@make_cached
def calc(a, b):
    # ...
    # ...
    print "calc({}, {})".format(a, b)
    return 42

# decorator
# calc = make_cached(calc)

def main():

    calc(3, 5)
    calc(2, 7)
    calc(3, 5)


if __name__ == '__main__':
    main()
