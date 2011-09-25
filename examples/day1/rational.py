class Rational(object):
    
    def __init__(self, numerator, denominator):
        self._n = numerator
        self._d = denominator

    @property
    def n(self):
	return self._n

    def __add__(self, other):
        return Rational(self._n * other._d + other._n * self._d,
                        self._d * other._d)

    def __repr__(self):
        return "<Rational {}/{}>".format(self._n, self._d)

    def __str__(self):
        return "{}/{}".format(self._n, self._d)



if __name__ == '__main__':
     
    half  = Rational(1, 2)
    third = Rational(1, 3)

    total = half + third
    total.n

    print "{} + {} = {}".format(half, third, total)
