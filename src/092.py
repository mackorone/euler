from collections import defaultdict
from functools import lru_cache


def sum_of_squares_of_digits(n):
    return sum(int(d) ** 2 for d in str(n))


@lru_cache(maxsize=None)
def get_terminal_number(n):
    if n in [0, 1, 89]:
        return n
    return get_terminal_number(sum_of_squares_of_digits(n))


def ans():
    # Bucket numbers 1 to 99,999 based on their
    # first iteration of get_terminal_number()
    groups = defaultdict(int)
    for n in range(100000):
        groups[sum_of_squares_of_digits(n)] += 1
    # Iterate over each bucket, add the remaining digits, check
    # whether or not the result of get_terminal_number() is 89
    total = 0
    for value, count in groups.items():
        for i in range(100):
			# n represents all numbers in a bucket
            n = sum_of_squares_of_digits(i) + value
            if get_terminal_number(n) == 89:
                total += count
    return total
    

if __name__ == '__main__':
    print(ans())
