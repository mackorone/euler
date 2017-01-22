def digit_sum(n):
    return sum(int(d) for d in str(n))


def ans():
    largest = 0
    for a in range(1, 101):
        for b in range(1, 101):
            largest = max(largest, digit_sum(a ** b))
    return largest
    

if __name__ == '__main__':
    print(ans())
