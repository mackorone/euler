from path import dirpath


_TRIANGLE_NUMS = [1, 3]
_PENTAGONAL_NUMS = [1, 5]
_HEXAGONAL_NUMS = [1, 6]


def _append_one_triangle():
    _TRIANGLE_NUMS.append(
        2 *_TRIANGLE_NUMS[-1] - _TRIANGLE_NUMS[-2] + 1
    )


def _append_one_pentagonal():
    _PENTAGONAL_NUMS.append(
        2 *_PENTAGONAL_NUMS[-1] - _PENTAGONAL_NUMS[-2] + 3
    )


def _append_one_hexagonal():
    _HEXAGONAL_NUMS.append(
        2 *_HEXAGONAL_NUMS[-1] - _HEXAGONAL_NUMS[-2] + 4
    )


def _nums(list_, append_func, end=None):
    index = 0
    while list_[index] < end if end is not None else True:
        yield list_[index]
        index += 1
        while len(list_) <= index:
            append_func()


def triangle_nums(end=None):
    return _nums(_TRIANGLE_NUMS, _append_one_triangle, end)
        
    
def pentagonal_nums(end=None):
    return _nums(_PENTAGONAL_NUMS, _append_one_pentagonal, end)
        
    
def hexagonal_nums(end=None):
    return _nums(_HEXAGONAL_NUMS, _append_one_hexagonal, end)
        

def _is(list_, append_func, n):
    while list_[-1] < n:
        append_func()
    return n in set(list_)


def is_triangle(n):
    return _is(_TRIANGLE_NUMS, _append_one_triangle, n)


def is_pentagonal(n):
    return _is(_PENTAGONAL_NUMS, _append_one_pentagonal, n)


def is_hexagonal(n):
    return _is(_HEXAGONAL_NUMS, _append_one_hexagonal, n)
