def ans():
    total = 0
    (x, y) = (1, 2)
    while x < 4000000:
        if x % 2 == 0:
            total += x
        (x, y) = (y, x + y)
    return total


if __name__ == '__main__':
    print(ans())
