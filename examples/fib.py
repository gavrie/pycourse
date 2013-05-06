# 1 1 2 3 5 8

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

