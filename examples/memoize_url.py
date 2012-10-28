def make_cached_func(func):
    cache = {}

    def cached_func(*args):
        key = args
        if key in cache:
            print "Returning data from cache for {}".format(args)
            return cache[key]

        data = func(key)
        cache[key] = data
        return data

    return cached_func

############

@make_cached_func
def fetchquote(stock, company):
    return "..."

@make_cached_func
def fetchurl(url):
    print "Fetching url {}".format(url)
    return "Data for url {}".format(url)

fetchurl("http://xx")
fetchurl("http://yy")
fetchurl("http://xx")
