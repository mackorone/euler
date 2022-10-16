from files import filepath
from functools import lru_cache


@lru_cache(maxsize=None)
def helper(triangle, row, col):
    if row == len(triangle):
        return 0
    return triangle[row][col] + max(
        helper(triangle, row + 1, col),
        helper(triangle, row + 1, col + 1),
    )


def max_sum_through_triangle(filename):
    lines = open(filepath(filename)).readlines()
    triangle = tuple([
        tuple([
            int(x) for x in line.split()
        ]) for line in lines
    ])
    return helper(triangle, 0, 0)
