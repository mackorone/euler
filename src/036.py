from palindrome import is_palindrome


def ans():
    sum_ = 0
    for i in range(1000000):
        if (
            is_palindrome(str(i)) and
            is_palindrome("{0:b}".format(i))
        ):
            sum_ += i
    return sum_
    

if __name__ == '__main__':
    print(ans())
