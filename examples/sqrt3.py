def square(x):
    return x * x


def average(x, y):
    return (x + y) / 2


def sqrt(x):
    def good_enough(guess):
        return abs(square(guess) - x) < 0.001

    def sqrt_iter(guess):
        def improve():
            return average(guess, x / guess)

        return (guess
                if good_enough(guess)
                else sqrt_iter(improve()))

    return sqrt_iter(1.0)


if __name__ == '__main__':
    print(sqrt(9.0))
