from itertools import count


def ans():
    limit = 1000
    total = 0
    for power in count(1):
        for num in count(1):
            length = len(str(num ** power))
            if length == power:
                total += 1
            elif power < length:
                break
        if limit < power:
            break
    return total
    

if __name__ == '__main__':
    print(ans())
