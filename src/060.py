from itertools import combinations
from prime import Prime


def compatible(one, two):
    return (
        Prime.contains(int(str(one) + str(two))) and
        Prime.contains(int(str(two) + str(one)))
    )


def remarkable(tuple_):
    for one, two in combinations(tuple_, 2):
        if not compatible(one, two):
            return False
    return True


def ans():
    size = 5
    skip_to = 8300
    for p in Prime.gen_nums():
        if p < skip_to:
            continue
        nums = [q for q in Prime.gen_nums(p) if compatible(q, p)]
        for tuple_ in combinations(nums, size - 1):
            if remarkable(tuple_):
                return p + sum(tuple_)


if __name__ == '__main__':
    print(ans())
