from path import dirpath


def ans():
    lines = open(dirpath() + '054.txt').readlines()
    cards = [line.strip().split() for line in lines]
    
    return None
    

if __name__ == '__main__':
    print(ans())
