import math

class Point(object):
    def __init__(self, _x, _y):
        self._x, self._y = _x, _y

    @property
    def x(self):
        return self._x

    @classmethod
    def bar(cls):
        cls.a = 5

    @staticmethod
    def foo():
        return 42

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

    def __repr__(self):
        return "<Point({}, {})>".format(self._x, self._y)

    def __sub__(self, other):
        return math.sqrt((self._x-other._x)**2 +
                         (self._y-other._y)**2)

    def __eq__(self, other):
        epsilon = 0.00001
        return self - other < epsilon

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(3, 4)

    assert p3 == p2
    print p1 - p2
    print repr(p1)
    print p2

    print p2.x
    p2.x = 5










