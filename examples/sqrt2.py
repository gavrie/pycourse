def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2


def sqrt(x):

    def good_enough(guess, x):
        return abs(square(guess) - x) < 0.001

    def sqrt_iter(guess, x):
        def improve(guess, x):
            return average(guess, x / guess)

        return guess if good_enough(guess, x) \
                     else sqrt_iter(improve(guess, x), x)

    return sqrt_iter(1.0, x)


if __name__ == '__main__':
    print sqrt(9.0)

