from math import factorial


def ans():
    sum_ = 0
    for i in range(3, 50000):
        if i == sum(factorial(int(c)) for c in str(i)):
            sum_ += i
    return sum_ 

if __name__ == '__main__':
    print(ans())
