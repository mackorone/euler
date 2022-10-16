from collections import defaultdict
from itertools import count


def ans():
    groups = defaultdict(list)
    for num in count():
        num_cubed = num ** 3
        key = tuple(sorted(str(num_cubed)))
        groups[key].append(num_cubed)
        if len(groups[key]) == 5:
            return groups[key][0]
    

if __name__ == '__main__':
    print(ans())
