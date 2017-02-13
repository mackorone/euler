from figurate import Pentagonal
from tuples import gen_tuples


def ans():
    for pair in gen_tuples():
        if pair[0] < 2100:
            continue
        one = Pentagonal.nth(pair[0])
        two = Pentagonal.nth(pair[1])
        if (
            Pentagonal.contains(one + two) and
            Pentagonal.contains(one - two)
        ):
            return one - two
    

if __name__ == '__main__':
    print(ans())
