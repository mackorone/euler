from prime import Prime


def ans():
    circular_primes = set([2])
    for p in Prime.gen_nums(1000000):
        if any(x in str(p) for x in '02468'):
            continue
        is_circular = True
        for i in range(len(str(p))):
            if not Prime.contains(int(str(p)[i:] + str(p)[:i])):
                is_circular = False
                break
        if is_circular:
            circular_primes.add(p)
    return len(circular_primes)
    

if __name__ == '__main__':
    print(ans())
