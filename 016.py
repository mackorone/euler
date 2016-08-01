def ans():
    num = 2 ** 1000
    return sum(int(x) for x in str(num))
    

if __name__ == '__main__':
    print(ans())
