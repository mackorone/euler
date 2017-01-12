from functools import lru_cache
from math import (
    ceil,
    sqrt,
)
from sequence import Sequence


class Prime(Sequence):

    _NUMS = [2, 3]

    @classmethod
    def _append(cls):
        cls._append_many()

    @classmethod
    def _append_one(cls):
       (candidate, flag) = (cls._NUMS[-1], False)
       while not flag:
           (candidate, flag) = (candidate + 2, True)
           end = int(sqrt(candidate)) + 1
           for prime in cls._NUMS:
               if end < prime:
                   break
               if candidate % prime == 0:
                   flag = False
                   break
       cls._NUMS.append(candidate)

    @classmethod
    def _append_many(cls): 
        largest = cls._NUMS[-1]
        lower_bound = largest + 1
        upper_bound = largest * 2 + 1
        candidates = [True] * (upper_bound - lower_bound)
        for prime in cls._NUMS:
            lowest_multiple = int(ceil(lower_bound / prime)) * prime
            for i in range(lowest_multiple, upper_bound, prime):
                candidates[i - lower_bound] = False
        for i in range(len(candidates)):
            if candidates[i]:
                cls._NUMS.append(i + lower_bound)

    @classmethod
    @lru_cache(maxsize=None)
    def contains(cls, n):
        if n < 2:
            return False
        end = int(sqrt(n)) + 1
        while cls._NUMS[-1] < end:
            cls._append()
        for p in cls.nums(end):
            if n % p == 0:
                return False
        return True
