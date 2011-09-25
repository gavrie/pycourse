class MyContext(object):
    
    def __init__(self):
        print ">> initialized"
    
    def __enter__(self):
        print ">> entered"
        return "something"
    
    def __exit__(self, *args):
        print ">> exited with: ", args
        return True


if __name__ == "__main__":
    with MyContext() as obj:
        print obj
