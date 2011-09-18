def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2

def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def improve(guess, x):
    return average(guess, x / guess)

def sqrt(x, guess=1.0):
    while not good_enough(guess, x):
        guess = improve(guess, x)
    return guess 

if __name__ == '__main__':
    print sqrt(9.0)

