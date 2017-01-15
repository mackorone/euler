def helper(num):
    return ''.join(sorted(str(num)))


def ans():
    num = 100000
    while True:
        string = helper(num)
        if all(helper(num * i) == string for i in range(2, 7)):
            return num
        num += 1
    

if __name__ == '__main__':
    print(ans())
