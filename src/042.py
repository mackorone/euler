from path import dirpath


_TRIANGLE_NUMS = [1, 3]


def is_triangle(n):
    while _TRIANGLE_NUMS[-1] < n:
        next_ = 2 *_TRIANGLE_NUMS[-1] - _TRIANGLE_NUMS[-2] + 1
        _TRIANGLE_NUMS.append(next_)
    return n in set(_TRIANGLE_NUMS)


def ans():
    words = open(dirpath() + '042.txt').read().split()
    count = 0
    for word in words:
        value = sum(ord(c) - ord('A') + 1 for c in word)
        if is_triangle(value):
            count += 1
    return count
    

if __name__ == '__main__':
    print(ans())
