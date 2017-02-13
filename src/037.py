from prime import Prime


def is_truncatable(n):
    str_n = str(n)
    if len(str_n) < 2:
        return False
    for i in range(1, len(str(n))):
        if not Prime.contains(int(str_n[:i])):
            return False
        if not Prime.contains(int(str_n[i:])):
            return False
    return True


def ans():
    truncatable = set()
    for p in Prime.gen_nums():
        if is_truncatable(p):
            truncatable.add(p)
        if len(truncatable) == 11:
            break
    return sum(truncatable)
    

if __name__ == '__main__':
    print(ans())
