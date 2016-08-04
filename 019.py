def num_days(month, year):
    feb_days = (
        29 if (
            year % 4 == 0 and (
                year % 100 != 0 or
                year % 400 == 0
            )
        ) else 28
    )
    return [
        31, feb_days, 31, 30,
        31,       30, 31, 31,
        30,       31, 30, 31,
    ][month]


def ans():
    total = 0
    cur_day = 2  # Jan 1. 1901 was a Tuesday
    for year in range(1901, 2001):
        for month in range(12):
            if cur_day == 0:
                total += 1
            cur_day += num_days(month, year)
            cur_day %= 7
    return total
    

if __name__ == '__main__':
    print(ans())
