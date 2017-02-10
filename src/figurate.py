from sequence import Sequence


class Figurate(Sequence):
    @classmethod
    def _append(cls):
        cls._NUMS.append(
            cls._NUMS[-1] * 2 - cls._NUMS[-2] +
            cls._NUMS[ 1] - 1 - cls._NUMS[ 0]
        )


class Triangle(Figurate):
    _NUMS = [1, 3]


class Pentagonal(Figurate):
    _NUMS = [1, 5]


class Hexagonal(Figurate):
    _NUMS = [1, 6]
