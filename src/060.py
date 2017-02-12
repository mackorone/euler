from itertools import count
from prime import Prime
from tuples import get_sequence_of_pairs
from tuples import get_sequence_of_triples


def ans():

    for i in get_sequence_of_triples().nums():
        print(i)
        if any(x > 20 for x in i):
            break
    return None

    nums = [3, 7, 109, 673]
    for p in Prime.nums():
        print(p)
        if p <= nums[-1]:
            continue
        all_primes = True
        for n in nums:
            if not (
                Prime.contains(int(str(p) + str(n))) and
                Prime.contains(int(str(n) + str(p)))
            ):
                all_primes = False
                break
        if all_primes:
            return p
    
    return None
    

if __name__ == '__main__':
    print(ans())
