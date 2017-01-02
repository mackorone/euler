from fib import (
    fib_index,
    next_fib,
)


def ans():
    return fib_index(next_fib(int('9' * 999)))
    

if __name__ == '__main__':
    print(ans())
