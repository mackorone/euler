from figurate import Pentagonal


def indices():
    start = 3000
    x = start
    y = start
    while True:
        yield (x, y)
        if x - 1 <= y + 1:
            start += 1
            x = start
            y = 1
        else:
            x -= 1
            y += 1
     

def ans():
    for pair in indices():
        one = Pentagonal.nth(pair[0])
        two = Pentagonal.nth(pair[1])
        if (
            Pentagonal.contains(one + two) and
            Pentagonal.contains(one - two)
        ):
            return pair[0] - pair[1]
    

if __name__ == '__main__':
    print(ans())
