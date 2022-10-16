from itertools import permutations


def ans():
    perms = permutations('0123456789')
    for i, x in enumerate(perms):
        if i == 999999:
            return ''.join(x)
    

if __name__ == '__main__':
    print(ans())
