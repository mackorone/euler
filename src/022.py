from path import dirpath


def get_value(name):
    return sum(
        ord(c) - ord('A') + 1 for
        c in name
    )


def ans():
    names = sorted(open(dirpath() + '022.txt').read().split())
    total = 0
    for i, name in enumerate(names):
        total += (i + 1) * get_value(name)
    return total
    

if __name__ == '__main__':
    print(ans())
