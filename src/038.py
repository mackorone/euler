from pandigital import is_pandigital


def ans():
    largest = 0
    for i in range(10000):
        string = ''
        for product in [i * j for j in range(1, 10)]:
            string += str(product)
            if 9 < len(string):
                break
            if (
                9 == len(string) and
                is_pandigital(string) and
                largest < int(string)
            ):
                largest = int(string)
    return largest
    

if __name__ == '__main__':
    print(ans())
