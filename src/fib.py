from bisect import bisect_right


_FIBS = [1, 1]


def _append_one():
    _FIBS.append(sum(_FIBS[-2:]))


def is_fib(n):
    """ Returns True if n is a fibonacci number, False otherwise
    """
    while _FIBS[-1] < n:
        _append_one()
    return n in set(_FIBS)


def next_fib(n):
    """ Returns the next fibonacci number greater than n
    """
    while _FIBS[-1] <= n:
        _append_one()
    return _FIBS[bisect_right(_FIBS, n)]


def fib_index(n):
    """ Returns the index of the fibonacci number n (zero-indexed)
    """
    if not is_fib(n):
        raise Exception
    return _FIBS.index(n)
