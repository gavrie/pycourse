# Website:
# https://github.com/gavrie/pycourse

def make_cached(func):
    cache = {}

    def cached(*key):
        if key in cache:
            result = cache[key]
        else:
            result = func(*key)
            cache[key] = result
        return result

    return cached

def main():
    @make_cached
    def calc(a, b):
        print "Running calc({}, {})".format(a, b)
        return a + b

    def calc2(a, b):
        print "Running calc2({}, {})".format(a, b)
        return a - b
    calc2 = make_cached(calc2)

    print calc(3, 4)
    print calc(4, 5)
    print calc(3, 4)

if __name__ == '__main__':
    main()

