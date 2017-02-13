def gen_diagonals():
    yield (1,)
    incs = [2, 4, 6, 8]
    nums = [3, 5, 7, 9]
    while True:
        yield tuple(nums)
        for i in range(4):
            incs[i] += 8
            nums[i] += incs[i]
