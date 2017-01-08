from path import dirpath
from shape import is_triangle


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
