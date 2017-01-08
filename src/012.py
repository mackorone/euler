from divisor import get_divisors
from shape import triangle_nums
    

def ans():
    for num in triangle_nums():
        if 500 <= len(get_divisors(num)):
            return num
    

if __name__ == '__main__':
    print(ans())
