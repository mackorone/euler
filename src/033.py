def ans():
    fractions = set()
    for num in range(10, 99):
        for den in range(num + 1, 100):
            # for i in len(str(c)):
            print('{} / {}'.format(num, den))
    return None
    

if __name__ == '__main__':
    print(ans())
