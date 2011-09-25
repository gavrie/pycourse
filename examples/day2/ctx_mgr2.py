from contextlib import contextmanager

@contextmanager
def my_context():
    print ">> initialized"
    try:
        print ">> entering"
        yield "something"
    finally:
        print ">> leaving"

if __name__ == "__main__":
    with my_context() as obj:
        print obj
