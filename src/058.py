from prime import Prime
from spiral import gen_diagonals


def ans():
    diags = gen_diagonals()
    next(diags)
    i = 1
    prime_count = 0
    total_count = 1
    while True:
        for n in next(diags):
            if Prime.contains(n):
                prime_count += 1
            total_count += 1
        i += 2
        if prime_count / total_count < .1:
            break
    return i
    

if __name__ == '__main__':
    print(ans())
