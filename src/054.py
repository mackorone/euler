from collections import (
    defaultdict,
    namedtuple,
)
from path import dirpath


def value(rank):
    try:
        return int(rank)
    except ValueError:
        return 10 + 'TJQKA'.index(rank)


def sort_by_rank(hand):
    return list(reversed(sorted(
        hand,
        key=lambda card: value(card[0]),
    )))

    
def of_a_kind(hand, count):
    counts = defaultdict(list)
    for card in hand:
        counts[card[0]].append(card)
    filtered = {
        rank: cards for
        rank, cards in counts.items() if
        count <= len(cards)
    }
    if len(filtered) < 1:
        return None
    return max(
        filtered.values(),
        key=lambda cards: value(cards[0][0])
    )


def multi_of_a_kind(hand, first_grouping_func):
    first_group = first_grouping_func(hand)
    if not first_group:
        return None
    second_group = two_of_a_kind([
        card for card in hand if
        card not in first_group
    ])
    if not second_group:
        return None
    return first_group + second_group


def high_card(hand):
    return of_a_kind(hand, 1)


def two_of_a_kind(hand):
    return of_a_kind(hand, 2)


def three_of_a_kind(hand):
    return of_a_kind(hand, 3)


def four_of_a_kind(hand):
    return of_a_kind(hand, 4)


def two_pair(hand):
    return multi_of_a_kind(hand, two_of_a_kind)


def full_house(hand):
    return multi_of_a_kind(hand, three_of_a_kind)


def straight(hand):
    sorted_ = sorted([value(card[0]) for card in hand])
    if sorted_ == list(range(sorted_[0], sorted_[-1] + 1)):
        return sort_by_rank(hand)
    return None


def flush(hand):
    counts = defaultdict(list)
    for card in hand:
        counts[card[1]].append(card)
    for cards in counts.values():
        if len(cards) == 5:
            return sort_by_rank(cards)
    return None


def straight_flush(hand):
    return flush(hand) if straight(hand) else None


def list_less_than(list_one, list_two):
    for i in range(len(list_one)):
        first = list_one[i]
        second = list_two[i]
        if value(first[0]) < value(second[0]):
            return True
    return False


def one_wins(one, two):
    for func in [
        straight_flush,    
        four_of_a_kind,    
        full_house,
        flush,
        straight,
        three_of_a_kind,
        two_pair,
        two_of_a_kind,
        high_card,
    ]:
        list_one = func(one)
        list_two = func(two)
        if list_one:
            if not list_two:
                return True
            if list_less_than(list_one, list_two):
                return False
            if list_less_than(list_two, list_one):
                return True
            one = [c for c in one if c not in list_one]
            two = [c for c in two if c not in list_two]
        elif list_two:
            return False
    raise Exception('No clear winner')


def ans():
    lines = open(dirpath() + '054.txt').readlines()
    turns = [line.strip().split() for line in lines]
    num_one_wins = 0
    for cards in turns:
        one = cards[:5]
        two = cards[5:]
        if one_wins(one, two):
            num_one_wins += 1
    return num_one_wins
    

if __name__ == '__main__':
    print(ans())
