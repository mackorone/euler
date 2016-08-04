def get_value(name):
    return sum(
        ord(c) - ord('A') + 1 for
        c in name
    )


def ans():
    data = open('022.txt').read()
    names = sorted([
        name.strip('"') for
        name in data.split(',')
    ])
    total = 0
    for i, name in enumerate(names):
        total += (i + 1) * get_value(name)
    return total
    

if __name__ == '__main__':
    print(ans())
