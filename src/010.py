from prime import primes


def ans():
    return sum(primes(2000000))


if __name__ == '__main__':
    print(ans())
