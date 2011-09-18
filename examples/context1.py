class Connection(object):
    def __init__(self):
        print "Creating connection"

    def close(self):
        print "Closing connection"


class Closing(object):
    def __init__(self, x):
        self.x = x

    def __enter__(self):
        print "Start"

    def __exit__(self, *args):
        self.x.close()
        print "Done"


with Closing(Connection()) as myconn:
    print "In context"
    myconn
    

