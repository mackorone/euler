from fibonacci import next_fib


def ans():
    total = 0
    num = 1
    while num < 4000000:
        if num % 2 == 0:
            total += num
        num = next_fib(num)
    return total


if __name__ == '__main__':
    print(ans())
