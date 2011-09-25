def generate_even(item=0):
    while True:
        yield item
        item += 2


if __name__ == '__main__':
    for i in generate_even():
        print i
        if i > 100:
            break
