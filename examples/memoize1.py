##########

def make_cached(func):

    cache = {}

    def cached_func(*args):
        key = args
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return cached_func


##########

@make_cached
def calc(a, b):
    # ....
    result = 42 + a + b
    print "calc({}, {}) => {}".format(a, b, result)
    return result

# calc = make_cached(calc)

##########

def main():

    calc(3, 4)
    # ...
    calc(5, 6)
    calc(3, 4)

if __name__ == '__main__':
    main()
