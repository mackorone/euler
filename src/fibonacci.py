from sequence import Sequence


class Fibonacci(Sequence):

    _NUMS = [1, 1]

    @classmethod
    def _append(cls):
        cls._NUMS.append(sum(cls._NUMS[-2:]))
