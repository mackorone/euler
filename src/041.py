from prime import next_prime


def is_pandigital(x):
    if 9 < len(str(x)):
        return False
    for digit in range(len(str(x))):
        if str(digit + 1) not in str(x):
            return False
    return True


def ans():
    prime = 2
    largest = None
    while prime < 10000000:
        if is_pandigital(prime):
            largest = prime
        prime = next_prime(prime)
    return largest


if __name__ == '__main__':
    print(ans())
