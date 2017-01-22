from palindrome import is_palindrome


def is_lychrel(n):
    iterations = 0
    while True:
        n += int(''.join(reversed(str(n))))
        iterations += 1
        if is_palindrome(str(n)):
            return False
        if 50 < iterations:
            return True


def ans():
    return len([n for n in range(1, 10000) if is_lychrel(n)])
    

if __name__ == '__main__':
    print(ans())
