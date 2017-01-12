from collections import defaultdict


def ans():
    n = 1000
    squares = {x ** 2: x for x in range(n)}
    counts = defaultdict(int)
    for i in range(1, n // 2):
        for j in range(i, n - i):
            k = squares.get(i ** 2 + j ** 2)
            if k is not None and i + j + k <= n:
                counts[i + j + k] += 1
    return max(counts.items(), key=lambda x: x[1])[0]
    

if __name__ == '__main__':
    print(ans())
