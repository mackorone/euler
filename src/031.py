COINS = [200, 100, 50, 20, 10, 5, 2]


def num_combos(amount, index):
    if amount < COINS[-1]:
        return 1
    combos = 0
    while index < len(COINS):
        coin = COINS[index]
        remaining = amount - coin
        while 0 <= remaining:
            combos += num_combos(remaining, index + 1)
            remaining -= coin
        index += 1
    return combos + 1


def ans():
    return num_combos(200, 0)
    

if __name__ == '__main__':
    print(ans())
