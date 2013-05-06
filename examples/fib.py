# 1 1 2 3 5 8

import sys
import time

counter = 0

def fib(n):
    global counter
    counter = counter + 1
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

try:
    arg = int(sys.argv[1])
except (IndexError, ValueError):
    print "Usage: fib.py <int>"
    sys.exit(1)


start_time = time.time()
print fib(arg)
end_time = time.time()

print "counter: {}".format(counter)
print "time: {}".format(end_time - start_time)
