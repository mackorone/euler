from math import factorial


def ans():
    return sum(int(x) for x in str(factorial(100)))
    

if __name__ == '__main__':
    print(ans())
