def generate_even(item=0):
    while True:
        yield item
        item += 2

if __name__ == '__main__':
    e = generate_even()

    for i in range(10):
        print e.next()
