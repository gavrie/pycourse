try:
    open("/etc/suxxxdoers")
except (IOError, TypeError) as e:
    print "Could not open file:", e.errno
    if e.errno != 13:
        raise
finally:
    print "finally"
