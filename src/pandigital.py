from itertools import permutations


def _digits(from_, to):
    if not 0 <= from_ <= to <= 9:
        raise ValueError
    return '0123456789'[from_:to + 1]


def is_pandigital(n, from_=1, to=None):
    str_n = str(n)
    if to is None:
        to = len(str_n)
    return all(d in str_n for d in _digits(from_, to))


def gen_pandigitals(from_=1, to=9):
    perms = permutations(_digits(from_, to))
    for n in perms:
        if n[0] != '0':
            yield int(''.join(n))
