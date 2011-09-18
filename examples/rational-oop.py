class Rational(object):

    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        return Rational(self.n * other.d + other.n * self.d,
                        self.d * other.d)

    def __repr__(self):
        return "{}/{}".format(self.n, self.d)


if __name__ == '__main__':
     
    half  = Rational(1, 2)
    third = Rational(1, 3)

    total = half + third

    print "{} + {} = {}".format(half, third, total)
