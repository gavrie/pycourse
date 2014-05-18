class Point(object):
    """
    Represent a point with x,y coordinates.
    """

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return "<Point ({}, {})>".format(self._x, self._y)

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
