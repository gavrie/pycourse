import math

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "<Point({}, {})>".format(self.x, self.y)

    def __sub__(self, other):
        return math.sqrt((self.x-other.x)**2 +
                         (self.y-other.y)**2)

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










