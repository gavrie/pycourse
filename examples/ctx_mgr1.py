



class MyManager(object):
    
    def __init__(self):
        print "initialized"
    
    def __enter__(self):
        print "entered"
        return "something"
    
    def __exit__(self, *args):
        print "exited with: ", args


if __name__ == "__main__":
    
    mgr = MyManager()
    with mgr as obj:
        print obj

