from math import factorial


SIZE = 20


def ans():
    # Permuatations with duplicates (two groups of size SIZE)
    return factorial(SIZE * 2) // (factorial(SIZE) ** 2)
    

if __name__ == '__main__':
    print(ans())
