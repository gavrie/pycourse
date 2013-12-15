def make_cached(func):
    # lexical scoping

    cache = {}

    def cached_func(*args):
        key = args
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return cached_func

# decorator

@make_cached
def calc(a, b):
    print "calc({}, {})".format(a, b)
    return a + b

# calc = make_cached(calc)

def main():
    print calc(3, 4)
    print calc(5, 6)
    print calc(3, 4)

if __name__ == '__main__':
    main()
