from collections import defaultdict
from itertools import combinations
from prime import Prime
from tuples import gen_tuples


def ans():

    disqualified = defaultdict(set)

    for indices in gen_tuples(4):

        primes = None
        satisfies = True

        for i, j in combinations(indices, 2):

            if i in disqualified[j]:
                satisfies = False
                break

            if not primes:
                primes = {k: Prime.nth(k) for k in indices}
                print(list(reversed(sorted(list(primes.values())))))

            if not (
                Prime.contains(int(str(primes[i]) + str(primes[j]))) and
                Prime.contains(int(str(primes[j]) + str(primes[i])))
            ):
                disqualified[i].add(j)
                disqualified[j].add(i)
                satisfies = False
                break

        if satisfies:
            return sum(primes.values())
    

if __name__ == '__main__':
    print(ans())
