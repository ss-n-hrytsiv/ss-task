__author__ = 'Nazar Hrytsiv'

def task330():
    """Task 330 Have a number n. find all ideal number lower then n"""

    n = input("Enter n: ")
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


def represent_function(function, function_doc):
    while True:
        print('*' * 100)
        print('Function logic: ' + '\n' + function_doc)
        print('-' * 50)
        print("If you want to run a task, press 1")
        print('If you want to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_input = input("Choose action: ")

        try:
            user_input = int(user_input)
            if user_input==1:
                print("A list of numbers lower then n and is ideal", task330())
            else:
                continue

        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


def task_330_menu():
    represent_function(task330, task330.__doc__)


