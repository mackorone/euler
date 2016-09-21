ONES_DIGITS = [
        '', 'one',   'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine',
]


TENS_DIGITS = [
         '',    None,  'twenty', 'thirty',  'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
]


TEENS = [
        'ten',  'eleven',    'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
]


def num_to_word(n):

    ones = ''
    tens = ''
    hundreds = ''

    if 1 <= n:
        ones = ONES_DIGITS[int(str(n)[-1])]
    if 10 <= n % 100:
        if n % 100 < 20:
            ones = ''
            tens = TEENS[int(str(n)[-1])]
        else:
            tens = TENS_DIGITS[int(str(n)[-2])]
    if 100 <= n:
        hundreds = ONES_DIGITS[int(str(n)[-3])]
    
    return '{}{}{}{}{}'.format(
        hundreds,
        'hundred' if hundreds else '',
        'and' if hundreds and (tens or ones) else '',
        tens,
        ones,
    )
    

def ans():
    return sum(
        len(num_to_word(i)) for
        i in range(1, 1000)
    ) + len('onethousand')

if __name__ == '__main__':
    print(ans())
