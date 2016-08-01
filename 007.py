from prime import next_prime

def ans():
    n = 2
    for i in range(10000):
        n = next_prime(n)
    return n

if __name__ == '__main__':
    print(ans())
