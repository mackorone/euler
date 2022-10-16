from itertools import combinations
from prime import Prime


def ans():
    for prime in Prime.gen_nums():
        if prime < 120000:
            continue

        # Replace all combinations of digits
        list_ = list(str(prime))
        length = len(list_)
        for count in range(length):
            combs = combinations(range(length), count)
            for indices in combs:

                # Count the number of primes by replacing
                # the selected digits with some other digit
                generated_primes = set()
                for replacement in range(10):
                    copy = list_.copy()
                    for i in indices:
                        copy[i] = str(replacement)
                    number = int(''.join(copy))
                    if Prime.contains(number):
                        generated_primes.add(number)
                
                if 7 < len(generated_primes):
                    return min(generated_primes)
    

if __name__ == '__main__':
    print(ans())
