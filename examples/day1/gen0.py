class Counter(object):
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


def counter():
    value = 0
    while True:
        value += 1
        if value > 3:
            raise StopIteration
        yield value

