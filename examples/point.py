from math import sqrt

class Point(object):
    """
    Represents a Point with x, y coordinates.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point({}, {})>".format(self.x, self.y)

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __sub__(self, other):
        return self.distance(other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance(p2) == 5
    assert p1.distance(p2) == p1 - p2

def test_equals():
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    assert p1 == p2

def test_dict():
    p1 = Point(3, 4)
    p2 = Point(3, 4)

    d = {}
    d[p1] = 'p1'
    d[p2] = 'p2'

    assert len(d) == 1

if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    print p1.distance(p2)
    print p1 - p2

