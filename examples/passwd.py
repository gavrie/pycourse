import sys

try:
    filename = sys.argv[1]
except IndexError:
    print "Usage: passwd <filename>"
    sys.exit(1)

f = open(filename)

for line in f:
    # root:*:0:0:System Administrator:/var/root:/bin/sh
    fields = line.strip().split(':')
    username, _, _, _, fullname, _, _ = fields
    print username, fullname
