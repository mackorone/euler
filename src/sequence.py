from bisect import (
    bisect_left,
    bisect_right,
)


class Sequence(object):

    _NUMS = []

    @classmethod
    def _append(cls):
        raise NotImplementedError

    @classmethod
    def nums(cls, end=None):
        n = cls._NUMS[0]
        while n < end if end is not None else True:
            yield prime
            n = cls.next_after(n)

    @classmethod
    def contains(cls, n):
        """ Returns whether or not n is in the sequence
        """
        return cls.index(_NUMS, n) is not None

    @classmethod
    def index(cls, n):
        """ Returns the index of n in the sequence (zero-indexed)
        """
        while cls._NUMS[-1] < n:
            cls._append()
        index = bisect_left(cls._NUMS, n)
        if index < len(cls._NUMS) and cls._NUMS[index] == n:
            return index 
        return None

    @classmethod
    def after(cls, n):
        """ Returns the first value in the sequence greater than x
        """
        while cls._NUMS[-1] <= n:
            cls._append()
        return cls._NUMS[bisect_right(cls._NUMS, n)]
