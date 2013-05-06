# 1 1 2 3 5 8

cache = {}

def fib(n):
    if n < 2:
        return 1
    if n not in cache:
        cache[n] = fib(n-2) + fib(n-1)
    return cache[n]
