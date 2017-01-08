from prime import get_prime_factors


def check(start, count):
    for i in range(start, start + count):
        if len(get_prime_factors(i)) < count:
            return False 
    return True


def ans():
    count = 4
    start = 134000
    while True:
        start += 1
        if check(start, count):
            break
    return start
    

if __name__ == '__main__':
    print(ans())
