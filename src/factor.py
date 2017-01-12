from collections import Counter
from functools import (
    lru_cache,
    reduce,
)
from itertools import combinations
from prime import Prime


@lru_cache(maxsize=None)
def get_prime_factors(n):
    """ Returns the counts of each prime factor of n
    """
    if n == 1:
        return Counter()
    divisor = 2
    while n % divisor != 0:
        divisor = Prime.after(divisor)
    return Counter({divisor: 1}) + get_prime_factors(n // divisor)


def get_flat_prime_factors(n):
    """ Returns a sorted list of n's prime_factor, where each
    prime factor is repeated the number of times it divides n
    """
    prime_factors = get_prime_factors(n)
    return sorted([
        x for list_ in (
            [factor] * count for
            factor, count in prime_factors.items()
        ) for x in list_
    ])


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


def get_proper_divisors(n):
    """ Returns a set of all proper divisors of n
    """
    return get_divisors(n) - {n}
