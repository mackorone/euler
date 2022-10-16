from figurate import (
    Heptagonal,
    Hexagonal,
    Octagonal,
    Pentagonal,
    Square,
    Triangle,
)


def check(one, two):
    return str(one)[-2:] == str(two)[:2]


def double_check(acc):
    for i in range(len(acc)):
        if not check(acc[i - 1], acc[i]):
            return False
    return True


def recurse(acc, remaining):
    if not remaining and double_check(acc):
        return sum(acc)
    for i in range(len(remaining)):
        for num in remaining[i][1]:
            if not acc or check(acc[-1], num):
                result = recurse(
                    acc + [num],
                    remaining[:i] + remaining[i + 1:],
                )
                if result:
                    return result


def get_nums(cls, lower, upper):
    return [num for num in cls.gen_nums(upper) if lower < num]


def ans():
    lower = 999
    upper = 10000
    dims_and_nums = [
        (3, get_nums(Triangle, lower, upper)),
        (4, get_nums(Square, lower, upper)),
        (5, get_nums(Pentagonal, lower, upper)),
        (6, get_nums(Hexagonal, lower, upper)),
        (7, get_nums(Heptagonal, lower, upper)),
        (8, get_nums(Octagonal, lower, upper)),
    ]
    return recurse([], dims_and_nums)
        

if __name__ == '__main__':
    print(ans())
