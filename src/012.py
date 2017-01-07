from divisor import get_divisors
    

def ans():
    triangle_inc = 1
    triangle_num = 0
    while len(get_divisors(triangle_num)) < 500:
        triangle_num += triangle_inc
        triangle_inc += 1
    return triangle_num
    

if __name__ == '__main__':
    print(ans())
