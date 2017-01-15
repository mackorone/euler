from pandigital import is_pandigital
from pprint import pprint


def ans():
    products = set()
    for i in range(1, 2000):
        for j in range(i, 2000):
            product = i * j
            string = str(i) + str(j) + str(product)
            length = len(string)
            if 9 < length:
                break
            if is_pandigital(int(string), to=9):
                products.add(product)
    return sum(products)
    

if __name__ == '__main__':
    print(ans())
