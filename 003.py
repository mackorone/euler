from math import sqrt
from prime import is_prime

def ans():
    num = 600851475143
    end = int(sqrt(num)) + 1
    for i in reversed(range(2, end)):
        if num % i == 0 and is_prime(i):
            return i

if __name__ == '__main__':
    print(ans())
