from itertools import permutations


def get_groups(perm):
    node_indices = [
        (0, 5, 6),
        (1, 6, 7),
        (2, 7, 8),
        (3, 8, 9),
        (4, 9, 5),
    ]
    return [
        [perm[j] for j in node_indices[i]]
        for i in range(5)
    ]


def is_magic(groups):
    prev_sum = None
    for group in groups:
        sum_ = sum(group)
        if not prev_sum:
            prev_sum = sum_
        if sum_ != prev_sum:
            return False
        prev_sum = sum_
    return True


def serialize(groups):
    min_ = None
    index = None
    for i, group in enumerate(groups):
        if not min_ or group[0] < min_:
            min_ = group[0]
            index = i
    return int(''.join(
        str(num)
        for i in range(index, index + 5)
        for num in groups[i % 5]
    ))


def ans():
    # The insight is that a 16-digit string requires that the number 10 be an
    # exterior node. However, in that case, the exterior nodes must be numbers
    # 6-10 in order for the pentagon ring to be magic. Thus, rather than
    # iterating over all permutations for numbers 1 through 10, we can iterate
    # over 1 through 5 and 6 through 10 separately, which greatly reduces the
    # amount of computation required.
    magics = []
    interior_perms = list(permutations(range(1, 6)))
    exterior_perms = list(permutations(range(6, 11)))
    for in_perm in interior_perms:
        for ex_perm in exterior_perms:
            perm = ex_perm + in_perm
            groups = get_groups(perm)
            if is_magic(groups):
                magics.append(groups)
    return max(serialize(groups) for groups in magics)


if __name__ == '__main__':
    print(ans())
