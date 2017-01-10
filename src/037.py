from prime import (
    is_prime,
    primes,
)


def is_truncatable(n):
    str_n = str(n)
    if len(str_n) < 2:
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str_n[:i])):
            return False
        if not is_prime(int(str_n[i:])):
            return False
    return True


def ans():
    truncatable = set()
    for p in primes():
        if is_truncatable(p):
            truncatable.add(p)
        if len(truncatable) == 11:
            break
    return sum(truncatable)
    

if __name__ == '__main__':
    print(ans())
