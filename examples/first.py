i = 1

while True:

    if i % 2 == 0:
        print "even"
    elif i % 2 != 0:
        print "odd"
    else:
        print "neither"

    i = i + 1

    if i > 5:
        break
