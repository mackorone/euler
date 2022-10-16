from spiral import gen_diagonals


def ans():
    sum_ = 0
    diags = gen_diagonals()
    for i in range(501):
        sum_ += sum(next(diags))
    return sum_


if __name__ == '__main__':
    print(ans())
