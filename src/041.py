from prime import primes


def is_pandigital(x):
    if 9 < len(str(x)):
        return False
    for digit in range(len(str(x))):
        if str(digit + 1) not in str(x):
            return False
    return True


def ans():
    largest = None
    for prime in primes(10000000):
        if is_pandigital(prime):
            largest = prime
    return largest


if __name__ == '__main__':
    print(ans())
