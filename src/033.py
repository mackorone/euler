from fractions import Fraction


def check(num, den):
    original = Fraction(num, den)
    for num_index in range(2):
        for den_index in range(2):
            if str(num)[1 - num_index] != str(den)[1 - den_index]:
                continue
            canceled = Fraction(
                int(str(num)[num_index]),
                int(str(den)[den_index]),
            )
            if canceled == original:
                return True
    return False


def ans():
    product = Fraction(1, 1)
    for num in range(10, 99):
        if num % 10 == 0:
            continue
        for den in range(num + 1, 100):
            if den % 10 == 0:
                continue
            if check(num, den):
                product *= Fraction(num, den)
    return product.denominator
    

if __name__ == '__main__':
    print(ans())
