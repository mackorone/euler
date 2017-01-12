from factor import get_divisors
from figurate import Triangle
    

def ans():
    for num in Triangle.nums():
        if 500 <= len(get_divisors(num)):
            return num
    

if __name__ == '__main__':
    print(ans())
