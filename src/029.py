def ans():
    nums = set()
    for a in range(2, 101):
        for b in range(2, 101):
            nums.add(a ** b)
    return len(nums)
    

if __name__ == '__main__':
    print(ans())
