from prime import Prime


def ans():
    n = 2
    for i in range(10000):
        n = Prime.after(n)
    return n


if __name__ == '__main__':
    print(ans())
