from palindrome import is_palindrome


def ans():
    largest = 0
    for x in range(100, 999):
        for y in range(x, 999):
            product = x * y
            if is_palindrome(str(product)) and largest < product:
                largest = product
    return largest


if __name__ == '__main__':
    print(ans())
