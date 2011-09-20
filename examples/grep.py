import fileinput
import re
import sys

regex = sys.argv.pop(1)

for line in fileinput.input():
    if re.match(regex, line):
        print line,

