# task88a check does number 3 in our n^2
def task_88a():
    n = input("Check does number 3 in n^2\n\n"
              "Enter n for check:")
    n2 = pow(float(n), 2)
    is_three_in_n = "3" in str(n2)
    return is_three_in_n


# task88b, reverse number
def task_88b():
    n = input("Reverse the number \n\n"
              "Enter n:")
    return n[::-1]


# task330
def task330():
    n = input("Find the all ideal number lower then n"
              "Enter n:")
    n = int(n)
    list_of_numbers = []
    for i in range(0, n):
        number = 0
        for j in range(1, i):
            if i % j == 0:
                number += j
        if number == i:
            list_of_numbers.append(i)
    return list_of_numbers


