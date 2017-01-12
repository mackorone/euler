from fibonacci import Fibonacci


def ans():
    return Fibonacci.index(Fibonacci.after(int('9' * 999))) + 1
    

if __name__ == '__main__':
    print(ans())
