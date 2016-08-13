from prime import get_prime_factors


def ans():
    factors = {}
    for i in range(20):
        for factor, count in get_prime_factors(i + 1).items():
            if factors.get(factor, 0) < count:
                factors[factor] = count
    total = 1
    for factor, count in factors.items():
        for i in range(count):
            total *= factor
    return total


if __name__ == '__main__':
    print(ans())
