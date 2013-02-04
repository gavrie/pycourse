def make_cached(func):
    """
    Receives a function as argument, and creates a new function
    that caches the results. It returns the new function.
    """
    # lexical closure
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
    # ... heavy calculation
    print "calc({a}, {b})".format(a=a, b=b)
    return a + b

# decorator pattern
# calc = make_cached(calc)

print calc(3, 4)
print calc(5, 6)
print calc(3, 4)
