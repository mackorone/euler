from collections import defaultdict
from itertools import combinations
from prime import Prime


def ans():
    groups = defaultdict(set)
    for prime in Prime.gen_nums(10000):
        groups[''.join(sorted(str(prime)))].add(prime)
    for set_ in groups.values():
        for comb in combinations(set_, 3):
            seq = sorted(list(comb))
            if seq[0] < 1000:
                continue
            if (
                seq[2] + seq[0] == 2 * seq[1] and
                seq[0] != 1487
            ):
                return ''.join(str(n) for n in seq)
    

if __name__ == '__main__':
    print(ans())
