
import urllib2


def find_in_url(s, url):
    
    print "searching for '%s' in '%s'..." % (s, url)
    f = urllib2.urlopen(url)

    for line in f:
        print ".",
        if s in line:
            print "\n", line
            break
    else:
        print "\n", "did not find '%s'" % s

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com"
    find_in_url("http", url)
    find_in_url("ofer", url)
    