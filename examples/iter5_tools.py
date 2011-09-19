from itertools import combinations, cycle, chain, count, izip

def iter_combinations():
    print "iter_combinations:"
    for i,j,k in combinations("ABCDEF", 3):
        print i + j + k


def iter_count():
    print "iter_count_izip:"
    f = file(__file__)
    for c, line in izip(count(), f):
        print "{}. {}".format(c, line),


def iter_cycle():
    print "iter_cycle_izip:"
    f = file(__file__)
    for c, line in izip(cycle("ABCDE"), f):
        print "{}. {}".format(c, line),


def iter_chain():
    import os
    file_names = sorted(os.listdir(os.getcwd()))
    files = map(file, file_names)
    for line in chain(*files):
        print ">>>", line,

# pass

if __name__ == '__main__':
    #iter_combinations()
    #iter_count()
    #iter_cycle()
    iter_chain()