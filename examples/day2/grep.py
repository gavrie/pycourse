#!/usr/bin/env python2.7
import fileinput
import re
import sys

#def log(msg):
#    print msg
#import pdb
#pdb.set_trace()

regex = sys.argv.pop(1)

for line in fileinput.input():
    if re.search(regex, line):
        print line,

