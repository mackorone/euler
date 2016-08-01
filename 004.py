def is_pal(n):
    return str(n) == str(n)[::-1]

def ans():
    largest = 0
    for x in range(100, 999):
        for y in range(100, 999):
            product = x * y
            if is_pal(product) and largest < product:
                largest = product
    return largest

if __name__ == '__main__':
    print(ans())
