from factor import get_divisors
from functools import lru_cache


@lru_cache(maxsize=None)
def get_proper_divisors(i):
    return get_divisors(i) - {i}


def ans():
    total = 0
    already_counted = set()
    for i in range(10000):
        candidate = sum(get_proper_divisors(i))
        if (
            i != candidate and
            i == sum(get_proper_divisors(candidate))
        ):
            for num in [i, candidate]:
                if num not in already_counted:
                    total += num
                    already_counted.add(num)
    return total
    

if __name__ == '__main__':
    print(ans())
