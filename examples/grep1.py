"""
TODO:
"""

import sys
import re

progname, pattern, filename = sys.argv

with open(filename) as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            print line.strip()
