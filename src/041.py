from pandigital import is_pandigital
from prime import Prime


def ans():
    largest = None
    for prime in Prime.nums(10000000):
        if is_pandigital(prime):
            largest = prime
    return largest


if __name__ == '__main__':
    print(ans())
