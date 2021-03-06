from prime import Prime


def ans():
    prime_list = list(Prime.gen_nums(4000))
    longest = (0, 0)
    for i in range(len(prime_list)):
        sum_ = 0
        for j in range(i, len(prime_list)):
            sum_ += prime_list[j]                
            if 1000000 <= sum_:
                break
            if Prime.contains(sum_) and longest[1] < j - i + 1:
                longest = (sum_, j - i + 1)
    return longest[0]
            
    
if __name__ == '__main__':
    print(ans())
