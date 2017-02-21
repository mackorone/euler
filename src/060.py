from prime import Prime


def ans():
    size = 5
    groups = []
    for p in Prime.gen_nums():
        new_groups = []
        for group in groups:
            for e in group:
                if not (
                    Prime.contains(int(str(p) + str(e))) and
                    Prime.contains(int(str(e) + str(p)))
                ):
                    break
            else:
                new_groups.append(group | {p})
        for new_group in new_groups:
            if len(new_group) == size:
                return sum(new_group)
            groups.append(new_group)
        groups.append({p})


if __name__ == '__main__':
    print(ans())
