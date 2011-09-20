def generate_even(item=0):
    while True:
        yield item
        item += 2



def iter_find_in_files(s, files):
    for fn in files:
        for line in file(fn):
            if s in line:
                yield (line, fn)



if __name__ == '__main__':
    e = generate_even()

    for i in range(10):
        print e.next()
