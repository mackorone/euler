from bisect import (
    bisect_left,
    bisect_right,
)


def contains(list_, x):
    """ Returns whether or not x is in list_
    """
    return index(list_, x) is not None


def index(list_, x):
    """ Returns the index of x in list_
    """
    idx = bisect_left(list_, x)
    if idx < len(list_) and list_[idx] == x:
        return idx
    return None


def next_(list_, x):
    """ Returns the leftmost value in list_ greater than x
    """
    index = bisect_right(list_, x)
    return list_[index] if index < len(list_) else None
