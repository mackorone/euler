from itertools import combinations
from prime import Prime


def ans():
    # The insight is that n / phi(n) is minimized when n has a few, large prime
    # factors (n can't be prime, since prime numbers don't satisfy the
    # permutation criteria). Also, note that we don't actually have to compute
    # all of the numbers coprime with n to determine phi(n); instead we can use
    # the fact that n is a product of two primes to calculate phi(n) in
    # constant time.
    min_n = None
    min_value = None
    primes = Prime.gen_nums(10 ** 4)
    combos = combinations(primes, 2)
    for one, two in list(combos):
        n = one * two
        if 10 ** 7 <= n:
            continue
        num_coprimes = (one - 1) * (two - 1)
        if sorted(str(n)) == sorted(str(num_coprimes)):
            value = n / num_coprimes
            if not min_value or value < min_value:
                min_n = n
                min_value = value
    return min_n


if __name__ == '__main__':
    print(ans())
