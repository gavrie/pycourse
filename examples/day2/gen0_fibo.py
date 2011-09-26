# Generator
def generate_fib():
    a, b = 0, 1
    while a < 5:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    for i in generate_fib():
        print i
