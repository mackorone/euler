from figurate import Triangle
from path import dirpath


def ans():
    words = open(dirpath() + '042.txt').read().split()
    count = 0
    for word in words:
        value = sum(ord(c) - ord('A') + 1 for c in word)
        if Triangle.contains(value):
            count += 1
    return count
    

if __name__ == '__main__':
    print(ans())
