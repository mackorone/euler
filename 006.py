def ans():
    squared_sum = sum((x + 1) for x in range(100)) ** 2
    sum_squares = sum((x + 1) ** 2 for x in range(100))
    return squared_sum - sum_squares

if __name__ == '__main__':
    print(ans())
