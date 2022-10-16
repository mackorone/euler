def cycle_length(n):
    string = str(int('1' + '0' * 1100) // n)
    shift = 1
    while string[-100:] != string[:-shift][-100:]:
        shift += 1
    return shift


def ans():
    longest = (None, 0) 
    for i in range(2, 1001):
        length = cycle_length(i)
        if longest[1] < length:
            longest = (i, length)
    return longest[0]


if __name__ == '__main__':
    print(ans())
