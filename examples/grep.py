#!/usr/bin/env python2.7
import fileinput
import re
import sys

regex = sys.argv.pop(1)

for line in fileinput.input():
    if re.search(regex, line):
        print line,

