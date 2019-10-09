def task_num_107():
    """ Дано целое число m > 1 Получить наибольшое целое к, при котором 4^к < m """
    m = int(input('\'Task 107\' Input your natural number : '))
    counter = 1
    a = 4
    while a < m:
        a *= a
        counter += 1
    return counter