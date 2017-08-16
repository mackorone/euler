from fractions import Fraction


def ans():
    three_sevenths = Fraction(3, 7)
    min_distance = None
    min_numerator = None
    n = 420000
    d = 990000
    while d < 10 ** 6:
        if Fraction(n, d) < three_sevenths:
            n += 1
        elif three_sevenths <= Fraction(n, d):
            d += 1
        distance = three_sevenths - Fraction(n, d)
        if distance <= 0:
            continue
        if not min_distance or distance < min_distance:
            min_distance = distance
            min_numerator = n
    return min_numerator


if __name__ == '__main__':
    print(ans())
