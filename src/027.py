from prime import Prime


def f(n, a, b):
    return n ** 2 + a * n + b


def ans():
    lim = 1000
    largest = (None, None, 0)
    for a in range(-lim + 1, lim):
        for b in range(-lim, lim + 1):
            n = 0
            while Prime.contains(f(n, a, b)):
                n += 1
            if largest[2] < n:
                largest = (a, b, n)
    return largest[0] * largest[1]
    

if __name__ == '__main__':
    print(ans())
