from prime import Prime


def ans():
    return sum(Prime.nums(2000000))


if __name__ == '__main__':
    print(ans())
