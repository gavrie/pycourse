import math

def make_point(x, y):
    """
    Create a point with the provided x, y coordinates.
    """
    return (x, y)

def print_point(point):
    """
    Print the point.
    """
    x, y = point
    print "Point {}, {}".format(x, y)

def distance(point1, point2):
    """
    Return the distance between the two provided points.
    """
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def equals(point1, point2):
    """
    Returns True if the points are equal to within epsilon, False otherwise.
    """
    epsilon = 0.00001
    return distance(point1, point2) < epsilon









