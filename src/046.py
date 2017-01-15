from prime import Prime


def satisfies_conjecture(n):
    root = 1
    while 2 * root ** 2 < n:
        if Prime.contains(n - 2 * root ** 2):
            return True
        root += 1
    return False


def ans():
    num = 9
    while satisfies_conjecture(num):
        num += 2
        while Prime.contains(num):
            num += 2
    return num
    

if __name__ == '__main__':
    print(ans())
