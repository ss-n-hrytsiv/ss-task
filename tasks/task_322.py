def max_sum_dividers():
    '''знайти натуральне число від 1 до 10000 з максимальною сумою дільників'''

    sums = {}
    for i in range(1, 10000):
        sums[i] = 0
    
        for j in range(1, i + 1):
            if i % j == 0:
                sums[i] += j
    
    return max(sums, key=sums.get)
