from files import filepath


def ans():
    lines = open(filepath('008.txt')).readlines()
    chars = ''.join(x.strip() for x in lines)
    largest = 0
    for i in range(len(chars) - 12):
        product = 1
        for j in range(13):
            product *= int(chars[i + j])
        largest = max(largest, product)
    return largest


if __name__ == '__main__':
    print(ans())
