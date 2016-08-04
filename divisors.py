from functools import reduce
from itertools import combinations
from prime import get_flat_prime_factors


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
