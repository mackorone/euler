from functools import lru_cache


def get_next(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


@lru_cache(maxsize=None)
def get_seq_len(n):
    if n == 1:
        return 1
    return 1 + get_seq_len(get_next(n))


def ans():
    (max_length, num) = (0, 0)
    for i in range(1, 999999):
        seq_len = get_seq_len(i)
        if max_length < seq_len:
            (max_length, num) = (seq_len, i)
    return num
    

if __name__ == '__main__':
    print(ans())
