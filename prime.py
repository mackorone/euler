from bisect import bisect_right
from collections import defaultdict
from functools import reduce
from itertools import combinations
from math import sqrt


_PRIMES = [2, 3]


def _append():
    (candidate, flag) = (_PRIMES[-1], False)
    while not flag:
        (candidate, flag) = (candidate + 2, True)
        end = int(sqrt(candidate)) + 1
        for prime in _PRIMES:
            if end < prime:
                break
            if candidate % prime == 0:
                flag = False
                break
    _PRIMES.append(candidate)


def is_prime(n):
    """ Returns True if n is prime, False otherwise
    """
    if n < 2:
        return False
    end = int(sqrt(n)) + 1
    while _PRIMES[-1] < end:
        _append()
    return n in set(_PRIMES)


def next_prime(n):
    """ Returns the next prime number greater than n
    """
    while _PRIMES[-1] <= n:
        _append()
    return _PRIMES[bisect_right(_PRIMES, n)]


def get_prime_factors(n):
    """ Returns the counts of each prime factor of n
    """
    prime_factors = defaultdict(int)
    divisor = 2
    while 1 < n:
        if n % divisor == 0:
            prime_factors[divisor] += 1
            n //= divisor
        else:
            divisor = next_prime(divisor)
    return dict(prime_factors)


def flatten_prime_factors(prime_factors):
    """ map<prime_factor, count> -> list<prime_factor>
    (where each prime factor is repeated "count" times)
    """
    return sorted([
        x for list_ in (
            [factor] * count for
            factor, count in prime_factors.items()
        ) for x in list_
    ])


def get_flat_prime_factors(n):
    return flatten_prime_factors(get_prime_factors(n))


def get_divisors(n):
    """ Returns a set of all divisors of n
    """
    if n < 1:
        return set()
    flat_factors = get_flat_prime_factors(n)
    divisors = set([1, n])
    for i in range(len(flat_factors)):
        for comb in combinations(flat_factors, i + 1):
            divisors.add(reduce(lambda x, y: x * y, comb))
    return divisors
