class Reversable(object):

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.data.pop()
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    it = iter(Reversable('hello'))
    print next(it)
