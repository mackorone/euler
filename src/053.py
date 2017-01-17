from math import factorial


def ans():
    count = 0
    for n in range(1, 101):
        for r in range(n + 1):
            num = factorial(n) / (factorial(r) * factorial(n - r))
            if 1000000 < num:
                count += 1
    return count
    

if __name__ == '__main__':
    print(ans())
