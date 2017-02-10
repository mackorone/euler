from itertools import product
from path import dirpath


def contains_common_words(string):
    common_words = ['and', 'be' 'of', 'the', 'to']
    count = len([w for w in common_words if w in string.split()])
    return 3 <= count


def decrypt(key, string):
    message = [None] * len(string)
    for i in range(len(key)):
        for j in range(i, len(string), len(key)):
            message[j] = chr(ord(string[j]) ^ ord(key[i]))
    return ''.join(message)


def ans():

    content = open(dirpath() + '059.txt').read()
    ordinals = [int(x) for x in content.strip().split(',')]
    encrypted = ''.join([chr(x) for x in ordinals])

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    possible_keys = product(alphabet, repeat=3)

    for key in possible_keys:
        decrypted = decrypt(key, encrypted)
        if contains_common_words(decrypted):
            break

    return sum(ord(c) for c in decrypted)


if __name__ == '__main__':
    print(ans())
