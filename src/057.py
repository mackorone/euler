from fractions import Fraction


def ans():
    count = 0
    frac = Fraction(3, 2)
    for i in range(0, 1000):
        if len(str(frac.denominator)) < len(str(frac.numerator)):
            count += 1
        frac = 2 + Fraction(1, frac + 1) - 1
    return count
    

if __name__ == '__main__':
    print(ans())
