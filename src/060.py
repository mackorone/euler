from prime import Prime


def ans():
    size = 5
    groups = []
    for p in Prime.gen_nums():
        print(p)
        for group in groups:
            for e in group:
                if not (
                    Prime.contains(int(str(p) + str(e))) and
                    Prime.contains(int(str(e) + str(p)))
                ):
                    break
            else:
                group.add(p)
                if len(group) == size:
                    return list(group)
        groups.append({p})


if __name__ == '__main__':
    print(ans())
