#!/usr/bin/env python

a = 1

if a == 1:
    print a
elif a == 3:
    pass
else:
    print "whatever"


l = ['a', 'b', 'c']

for i, x in enumerate(l):
    if i%2 == 0:
        continue
    print i, x
    if i > 2:
        break


while l:
    print l.pop()











