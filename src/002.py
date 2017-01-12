from fibonacci import Fibonacci


def ans():
    total = 0
    num = 1
    while num < 4000000:
        if num % 2 == 0:
            total += num
        num = Fibonacci.after(num)
    return total


if __name__ == '__main__':
    print(ans())
