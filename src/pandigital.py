def is_pandigital(n):
    str_n = str(n)
    for digit in range(len(str_n)):
        if str(digit + 1) not in str_n:
            return False
    return True
