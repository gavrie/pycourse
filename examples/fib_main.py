import sys
import time

from fib import fib

def main():
    try:
        arg = int(sys.argv[1])
    except (IndexError, ValueError):
        print "Usage: fib.py <int>"
        sys.exit(1)

    start_time = time.time()
    print fib(arg)
    end_time = time.time()

    print "time: {}".format(end_time - start_time)

if __name__ == '__main__':
    main()
