def ans():
    lines = open('013.txt').readlines()
    sum_ = sum(int(line.strip()) for line in lines)
    return str(sum_)[:10]
    

if __name__ == '__main__':
    print(ans())
