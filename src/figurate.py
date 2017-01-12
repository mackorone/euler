from sequence import Sequence


class Figurate(Sequence):

    _INCREMENT = None

    @classmethod
    def _append(cls):
        cls._NUMS.append(2 * cls._NUMS[-1] - cls._NUMS[-2] + cls._INCREMENT)


class Triangle(Figurate):

    _NUMS = [1, 3]
    _INCREMENT = 1


class Pentagonal(Figurate):

    _NUMS = [1, 5]
    _INCREMENT = 3


class Hexagonal(Figurate):

    _NUMS = [1, 6]
    _INCREMENT = 4
