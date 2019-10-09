def task330():
    """Task 330 Have a number n find all ideal number lower then n"""

    n = input("Find the all ideal number lower then n\n\n"
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
