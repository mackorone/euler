from itertools import permutations
from pandigital import gen_pandigitals
from prime import Prime


def ans():
    divisors = list(Prime.gen_nums(18))
    sum_ = 0
    for p in gen_pandigitals(from_=0, to=9):
        has_property = True
        for i in range(1, 8):
            dividend = int(str(p)[i:i + 3])
            if dividend % divisors[i - 1] != 0:
                has_property = False
                break
        if has_property:
            sum_ += p
    return sum_
    

if __name__ == '__main__':
    print(ans())
