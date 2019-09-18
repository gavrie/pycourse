

MY_LIST = ["First Item", "Second Item", "Third Item", "Last Item"]

def main():
    it = iter(MY_LIST)
    while True:
        try:
            item = next(it)
        except Exception as e:
            break
        else:
            print item

if __name__=="__main__":
    print __file__
    main()
