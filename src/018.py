from functools import lru_cache
from path import dirpath


@lru_cache(maxsize=None)
def max_path_value(triangle, row, col):
    if row == len(triangle):
        return 0
    return triangle[row][col] + max(
        max_path_value(triangle, row + 1, col),
        max_path_value(triangle, row + 1, col + 1),
    )


def ans():
    lines = open(dirpath() + '018.txt').readlines()
    triangle = tuple([
        tuple([
            int(x) for x in line.split()
        ]) for line in lines
    ])
    return max_path_value(triangle, 0, 0)
    

if __name__ == '__main__':
    print(ans())
