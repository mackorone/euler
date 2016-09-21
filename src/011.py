LENGTH = 4


def helper(grid, row, col, row_inc, col_inc, length, acc):
    if length == LENGTH:
        return acc
    if not (
        0 <= row + row_inc < len(grid) and
        0 <= col + col_inc < len(grid[row + row_inc])
    ):
        return 0
    return helper(
        grid,
        row + row_inc,
        col + col_inc,
        row_inc,
        col_inc,
        length + 1,
        acc * grid[row][col]
    )


def ans():
    lines = open('011.txt').readlines()
    grid = [
        [int(x) for x in line.split()]
        for line in lines
    ]
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for row_inc, col_inc in [
                ( 1, 0),  # Vertical
                ( 0, 1),  # Horizonatal
                ( 1, 1),  # Diagonal one
                (-1, 1),  # Diagonal two
            ]:
                largest = max(
                    largest,
                    helper(grid, i, j, row_inc, col_inc, 0, 1),
                )
    return largest
    

if __name__ == '__main__':
    print(ans())
