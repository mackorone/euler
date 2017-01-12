from factor import get_proper_divisors


def is_abundant(n):
    return n < sum(get_proper_divisors(n))


def ans():
    abundants = {
        x for x in range(28123) if
        is_abundant(x)
    }
    sum_of_two = {
        x + y for
        x in abundants for
        y in abundants
    }
    return sum(
        x for x in range(28123) if
        x not in sum_of_two
    )
    

if __name__ == '__main__':
    # TODO: this can be improved
    print(ans())
