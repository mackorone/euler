from functools import (
    lru_cache,
    total_ordering,
)
from sequence import Sequence


# TODO: MACK - update 044.py


# TODO: won't need this if we memoize get_sequence_of_tuples
# TODO: This should encode boolean parameters too
DIMS_TO_SEQS = {
}


def indexof(tuple_):  # TODO
    if len(tuple_) == 1:
        return tuple_[0]
    else:
        return DIMS_TO_SEQS[len(tuple_)].index(Tuple(*tuple_))


@total_ordering
class Tuple(object):

    # TODO: MACK - put index in here for perf?

    def __init__(self, *args):
        self.tuple_ = tuple(args)

    def __getitem__(self, key):
        return self.tuple_[key]
        
    def __eq__(self, other):
        return self.tuple_ == other.tuple_

    def __lt__(self, other):

        self_len = len(self.tuple_)
        other_len = len(other.tuple_)
        if self_len != other_len:
            return self_len < other_len

        self_head = self.tuple_[:-1]
        self_tail = self.tuple_[-1]
        self_sum = indexof(self_head) + self_tail

        other_head = other.tuple_[:-1]
        other_tail = other.tuple_[-1]
        other_sum = indexof(other_head) + other_tail

        if self_sum != other_sum:
            return self_sum < other_sum

        return self_tail < other_tail
            
    def __repr__(self):
        return str(self.tuple_)


@lru_cache(maxsize=None)
def get_sequence_of_pairs(
    starting_num=1,
    enforce_unique=False,
    enforce_sorted=False,
):
    class SequenceOfPairs(Sequence):

        _NUMS = [Tuple(
            starting_num + 1 * int(enforce_unique),
            starting_num + 0 * int(enforce_unique))]

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


def get_sequence_of_triples(
    starting_num=1,
    enforce_unique=False, # TODO: allow dupliacates
    enforce_sorted=False, # TODO: order doesn't matter
):
    class SequenceOfTriples(Sequence):

        _NUMS = [Tuple(
            starting_num + 2 * int(enforce_unique),
            starting_num + 1 * int(enforce_unique),
            starting_num + 0 * int(enforce_unique))]

        _PAIRS = get_sequence_of_pairs(
            starting_num,
            enforce_unique,
            enforce_sorted,
        )

        DIMS_TO_SEQS[2] = _PAIRS
        _INDEX = 1

        @classmethod
        def _append(cls):
            cls._INDEX += 1
            index, num = DIMS_TO_SEQS[2].nth(cls._INDEX)
            x, y = DIMS_TO_SEQS[2].nth(index)
            while (
                (enforce_unique and any([num == v for v in DIMS_TO_SEQS[2].nth(index)])) or
                (enforce_sorted and y < num) # second - last num is less than last num
            ):
                cls._INDEX += 1
                index, num = DIMS_TO_SEQS[2].nth(cls._INDEX)
                x, y = DIMS_TO_SEQS[2].nth(index)
            cls._NUMS.append(Tuple(x, y, num))

    return SequenceOfTriples



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
