from prime import next_prime

def ans():
    total = 0
    num = 2
    while num < 2000000:
        total += num
        num = next_prime(num)
    return total

if __name__ == '__main__':
    print(ans())
