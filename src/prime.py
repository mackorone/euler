from bisect import bisect_right
from collections import defaultdict
from math import (
    ceil,
    sqrt,
)


_PRIMES = [2, 3]


def _append_one():
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


def _append_many(): 
    largest = _PRIMES[-1]
    lower_bound = largest + 1
    upper_bound = largest * 2 + 1
    candidates = [True] * (upper_bound - lower_bound)
    for prime in _PRIMES:
        lowest_multiple = int(ceil(lower_bound / prime)) * prime
        for i in range(lowest_multiple, upper_bound, prime):
            candidates[i - lower_bound] = False
    for i in range(len(candidates)):
        if candidates[i]:
            _PRIMES.append(i + lower_bound)


def primes(end=None):
    """ Returns a generator for the prime numbers
    """
    prime = next_prime(0)
    while prime < end if end is not None else True:
        yield prime
        prime = next_prime(prime)


def is_prime(n):
    """ Returns True if n is prime, False otherwise
    """
    if n < 2:
        return False
    end = int(sqrt(n)) + 1
    while _PRIMES[-1] < end:
        _append_many()
    for p in primes(end):
        if n % p == 0:
            return False
    return True


def next_prime(n):
    """ Returns the next prime number greater than n
    """
    while _PRIMES[-1] <= n:
        _append_many()
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
