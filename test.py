def test():
    i = 0;
    while True:
        yield i
        i = i + 1

if __name__ == '__main__':
    x = test()
    for i in range(5):
        print(x.__next__())
