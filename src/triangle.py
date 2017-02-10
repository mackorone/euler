from files import filepath
from functools import lru_cache


@lru_cache(maxsize=None)
def max_path_value(triangle, row=0, col=0):
    if row == len(triangle):
        return 0
    return triangle[row][col] + max(
        max_path_value(triangle, row + 1, col),
        max_path_value(triangle, row + 1, col + 1),
    )


def get_triangle(filename):
    lines = open(filepath(filename)).readlines()
    triangle = tuple([
        tuple([
            int(x) for x in line.split()
        ]) for line in lines
    ])
    return triangle
