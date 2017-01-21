from collections import (
    defaultdict,
    namedtuple,
)
from path import dirpath


def _value(rank):
    try:
        return int(rank)
    except ValueError:
        return 10 + 'TJQKA'.index(rank)


def _sort_by_rank(hand):
    return list(reversed(sorted(
        hand,
        key=lambda card: _value(card[0]),
    )))

    
def _of_a_kind(hand, count):
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
        key=lambda cards: _value(cards[0][0])
    )


def high_card(hand):
    return _of_a_kind(hand, 1)


def two_of_a_kind(hand):
    return _of_a_kind(hand, 2)


def three_of_a_kind(hand):
    return _of_a_kind(hand, 3)


def four_of_a_kind(hand):
    return _of_a_kind(hand, 4)


def full_house(hand):
    three = three_of_a_kind(hand)
    if not three:
        return None
    pair = two_of_a_kind([card for card in hand if card not in three])
    if not pair:
        return None
    return three + pair


def straight(hand):
    sorted_ = sorted([_value(card[0]) for card in hand])
    if sorted_ == list(range(sorted_[0], sorted_[-1] + 1)):
        return _sort_by_rank(hand)
    return None


def flush(hand):
    counts = defaultdict(list)
    for card in hand:
        counts[card[1]].append(card)
    for cards in counts.values():
        if len(cards) == 5:
            return _sort_by_rank(cards)
    return None


def straight_flush(hand):
    return flush(hand) if straight(hand) else None


def ans():
    lines = open(dirpath() + '054.txt').readlines()
    turns = [line.strip().split() for line in lines]
    num_wins = 0
    for cards in turns:
        one = cards[:5]
        two = cards[5:]
    
    return None
    

if __name__ == '__main__':
    print(ans())
