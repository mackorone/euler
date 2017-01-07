def ans():
    nums = set()
    for i in range(2, 200000):
        if i == sum(int(c) ** 5 for c in str(i)):
            nums.add(i)
    return sum(nums)
    

if __name__ == '__main__':
    print(ans())
