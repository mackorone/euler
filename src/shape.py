from search import contains


_TRIANGLE_NUMS = [1, 3]
_PENTAGONAL_NUMS = [1, 5]
_HEXAGONAL_NUMS = [1, 6]


def _append_one(list_, increment):
    list_.append(2 * list_[-1] - list_[-2] + increment)


def _nums(list_, increment, end=None):
    index = 0
    while list_[index] < end if end is not None else True:
        yield list_[index]
        index += 1
        while len(list_) <= index:
            _append_one(list_, increment)


def triangle_nums(end=None):
    return _nums(_TRIANGLE_NUMS, 1, end)
        
    
def pentagonal_nums(end=None):
    return _nums(_PENTAGONAL_NUMS, 3, end)
        
    
def hexagonal_nums(end=None):
    return _nums(_HEXAGONAL_NUMS, 4, end)
        

def _is(list_, increment, n):
    while list_[-1] < n:
        _append_one(list_, increment)
    return contains(list_, n)


def is_triangle(n):
    return _is(_TRIANGLE_NUMS, 1, n)


def is_pentagonal(n):
    return _is(_PENTAGONAL_NUMS, 3, n)


def is_hexagonal(n):
    return _is(_HEXAGONAL_NUMS, 4, n)
