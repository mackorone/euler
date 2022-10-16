def ans():

    # Generate the string
    i = 1
    string = ''
    while len(string) < 1000000:
        string += str(i)
        i += 1

    # Calculate the product
    product = 1
    for power in range(7):
        index = 10 ** power - 1
        digit = int(string[index])
        product *= (digit)
    return product
    

if __name__ == '__main__':
    print(ans())
