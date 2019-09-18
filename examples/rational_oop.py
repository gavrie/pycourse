class Rational(object):

    def __init__(self, numerator, denominator):
        self.numer = numerator
        self.denom = denominator

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom,
                        self.denom * other.denom)

    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"

    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)

    def _decimal(self):
        return float(self.numer) / self.denom


if __name__ == '__main__':
    half = Rational(1, 2)
    third = Rational(1, 3)

    total = half + third

    print(f"{half} + {third} = {total}")
    print(f"{half!r} + {third!r} = {total!r}")
