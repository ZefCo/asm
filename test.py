def main():
    t = test
    t()



def test(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


def embedded_test(*args, **kwargs):
    pass


if __name__ in '__main__':
    main()