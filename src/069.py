from prime import Prime


def ans():
    n = 1
    for p in Prime.gen_nums():
        next_ = n * p
        if 1000000 < next_:
            return n
        n = next_
    return n
    

if __name__ == '__main__':
    print(ans())
