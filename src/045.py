from shape import (
    hexagonal_nums,
    pentagonal_nums,
    triangle_nums,
)


def ans():
    generators = (
        triangle_nums(),
        pentagonal_nums(),
        hexagonal_nums(),
    )
    nums = [next(g) for g in generators]
    while True:
        if len(set(nums)) == 1 and 40755 < nums[0]:
            return nums[0]
        index = nums.index(min(nums))
        nums[index] = next(generators[index])
    

if __name__ == '__main__':
    print(ans())
