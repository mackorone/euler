from enum import Enum


def next_(x, y):

    # Quadrant IV
    if 0 < x and y <= 0:
        if -y < x:
            return (x, y - 1)
        else:
            return (x - 1, y)

    # Quadrant III
    elif x <= 0 and y < 0:
        if -x < -y:
            return (x - 1, y)
        else:
            return (x, y + 1)

    # Quadrant II
    elif x < 0 and 0 <= y:
        if y < -x:
            return (x, y + 1)
        else:
            return (x + 1, y)

    # Quadrant I
    elif 0 <= x and 0 < y:
        if x <= y:
            return (x + 1, y)
        else:
            return (x, y - 1)

    # Origin
    else:
        return (x + 1, y)


def ans():

    width = 1001

    x = 0
    y = 0
    points = {}
    for i in range(1, width ** 2 + 1):
        points[(x, y)] = i
        (x, y) = next_(x, y)
    
    sum_ = points[(0, 0)]
    for i in range(1, width // 2 + 1):
        sum_ += points[(i, i)]
        sum_ += points[(i, -i)]
        sum_ += points[(-i, i)]
        sum_ += points[(-i, -i)]
    
    return sum_

if __name__ == '__main__':
    print(ans())
