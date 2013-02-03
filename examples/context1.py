class Connection(object):
    def __init__(self):
        print "Connection: Creating"

    def close(self):
        print "Connection: Closing"


class Closing(object):
    def __init__(self, x):
        self._x = x

    def __enter__(self):
        print ">> Entering context"
        return self._x

    def __exit__(self, *args):
        print ">> Leaving context"
        self._x.close()


with Closing(Connection()) as myconn:
    print "Inside context"
    myconn
    











