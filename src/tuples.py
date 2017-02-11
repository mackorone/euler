from functools import (
    lru_cache,
    total_ordering,
)
from sequence import Sequence


# TODO: MACK - update 044.py


@total_ordering
class Tuple(object):

    def __init__(self, *args):
        self.tuple_ = tuple(args)

    def __getitem__(self, index):
        return self.tuple_[index]
        
    def __eq__(self, other):
        return self.tuple_ == other.tuple_

    def __lt__(self, other):
        self_sum = sum(self.tuple_)
        other_sum = sum(other.tuple_)
        if self_sum != other_sum:
            return self_sum < other_sum
        return self.tuple_[-1] < other.tuple_[-1]
            
    def __repr__(self):
        return str(self.tuple_)


@lru_cache(maxsize=None)
def get_sequence_of_pairs(
    starting_num=1,
    enforce_unique=False,
    enforce_sorted=False,
):
    class SequenceOfPairs(Sequence):

        _NUMS = [Tuple(starting_num, starting_num)]
        _NEXT = starting_num
        _START = starting_num

        @classmethod
        def _append(cls):
            x, y = cls._NUMS[-1]
            x -= 1
            y += 1
            if enforce_unique and x == y:
                x -= 1
                y += 1
            if x < (y if enforce_sorted else cls._START):
                cls._NEXT += 1
                x = cls._NEXT
                y = cls._START
            cls._NUMS.append(Tuple(x, y))

    return SequenceOfPairs


def get_sequence_of_tuples(
    dimensions=3,
    starting_num=1,
    enforce_unique=False,
    enforce_sorted=False,
):
    dims_to_seqs = {
        2: get_sequence_of_pairs(
            starting_num,
            enforce_unique,
            enforce_sorted
        ),
    }

    for dim in range(len(dims_to_seqs) + 2, dimsensions + 1):

        class SequenceOfTuples(Sequence):

            _NUMS = [Tuple(starting_num, starting_num)]
            _NEXT = starting_num
            _START = starting_num

            @classmethod
            def _append(cls):
                x, y = cls._NUMS[-1]
                x -= 1
                y += 1
                if enforce_unique and x == y:
                    x -= 1
                    y += 1
                if x < (y if enforce_sorted else cls._START):
                    cls._NEXT += 1
                    x = cls._NEXT
                    y = cls._START
                cls._NUMS.append(Tuple(x, y))

        dims_to_seqs[dim] = SequenceOfTuples
    return dims_to_seqs[dimensions]
