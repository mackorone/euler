from prime import Prime


def ans():
    return sum(Prime.gen_nums(2000000))


if __name__ == '__main__':
    print(ans())
