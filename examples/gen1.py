def mygen():
    print "start"
    yield 1
    print "middle"
    yield 2
    print "end"
    yield 3


if __name__ == '__main__':

    for x in mygen():
        pass
