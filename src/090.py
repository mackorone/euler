from itertools import combinations


def can_display_all_cubes(one, two):
    one_extended = set(one)
    two_extended = set(two)
    for set_ in [one_extended, two_extended]:
        if 6 in set_ or 9 in set_:
            set_ |= {6, 9}
    for i in range(1, 10):
        digits = [int(n) for n in list(str(i ** 2).zfill(2))]
        if not (
            (digits[0] in one_extended and digits[1] in two_extended) or
            (digits[1] in one_extended and digits[0] in two_extended)
        ):
            return False
    return True


def ans():
    count = 0
    digits = list(range(10))
    combos = list(combinations(digits, 6))
    for i, one in enumerate(combos):
        for j, two in enumerate(combos):
            if j < i:
                continue
            if can_display_all_cubes(one, two):
                count += 1
    return count
    

if __name__ == '__main__':
    print(ans())
