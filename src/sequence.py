from bisect import (
    bisect_left,
    bisect_right,
)


class Sequence(object):

    _NUMS = None

    @classmethod
    def _append(cls):
        raise NotImplementedError

    @classmethod
    def nums(cls, end=None):
        """ Returns a generator for the sequence
        """
        n = cls._NUMS[0]
        while n < end if end is not None else True:
            yield n
            n = cls.after(n)

    @classmethod
    def nth(cls, n):
        """ Returns the nth element in the sequence (one-indexed)
        """
        if n < 1:
            raise IndexError
        while len(cls._NUMS) < n:
            cls._append()
        return cls._NUMS[n - 1]

    # TODO: MACK - use set?
    @classmethod
    def contains(cls, n):
        """ Returns whether or not n is in the sequence
        """
        return cls.index(n) is not None

    @classmethod
    def index(cls, n):
        """ Returns the index of n in the sequence (one-indexed)
        """
        while cls._NUMS[-1] < n:
            cls._append()
        index = bisect_left(cls._NUMS, n)
        if index < len(cls._NUMS) and cls._NUMS[index] == n:
            return index + 1
        return None

    @classmethod
    def after(cls, n):
        """ Returns the first value in the sequence greater than n
        """
        while cls._NUMS[-1] <= n:
            cls._append()
        return cls._NUMS[bisect_right(cls._NUMS, n)]
