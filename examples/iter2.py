

MY_LIST = ["First Item", "Second Item", "Third Item", "Last Item"]


class MyContainer(object):

    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, idx):
        return self.lst[idx]
    
    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        return MyIterator(self)

class MyIterator(object):

    def __init__(self, container):
        self.container = container
        self.idx = -1

    # Iterator Interfaces
    def next(self):
        self.idx += 1
        if self.idx >= len(self.container):
            raise StopIteration()
        return self.container[self.idx]

def main():
    container = MyContainer(MY_LIST)
    for item in container:
        print item

if __name__=="__main__":
    print __file__
    main()
