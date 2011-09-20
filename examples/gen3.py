import os
from time import sleep, time
from random import random
from functools import partial

class TimeoutException(Exception): pass

def iter_wait(predicates, timeout=None, sleep_time = 1.0):

    if timeout:
        deadline = time() + timeout
    else:
        deadline = None
    predicates = list(predicates)

    iterations = 0
    while True:
        # check the deadline
        if deadline and time() > deadline:
            raise TimeoutException("Did not meet all predicates within timeout ({})".format(timeout))

        # check the predicates
        predicates = [pred for pred in predicates if not pred()]
        if not predicates:
            return
        
        # prepare for next iteration
        iterations += 1
        
        # yield the generator
        yield "...waiting for {} predicates (iteration #{})".format(len(predicates), iterations)
        
        sleep(sleep_time)



def get_file_exists_predicate(fn):
    return partial(os.path.isfile, fn) 

def maybe_create_file(fn):
    r = random()
    if r > 0.8:
        with file(fn, "w") as f:
            f.write("random was {}".format(r))
        return True

def deal_with_files(fnames):
    fn = fnames.pop()
    if not maybe_create_file(fn):
        fnames.insert(0, fn)
    else:
        print "({} was created)".format(fn)

if __name__ == '__main__':

    fnames = ["a.txt","b.txt","c.txt","d.txt"]
    
    predicates = map(get_file_exists_predicate, fnames)
    for status in iter_wait(predicates, timeout = 100):
        print status
        deal_with_files(fnames)
    print "All files exist"
