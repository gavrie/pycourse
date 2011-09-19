

def iter_file():
    
    f = file(__file__)
    
    print "--- First Iteration {}".format(f)
    for line in f:
        print ">>", line, 
    
    print ""
    print "--- Second Iteration {}".format(f)
    for line in f:
        print ">>", line,
    else:
        print "Empty!"

if __name__ == '__main__':
    iter_file()