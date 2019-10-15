def max_sum_dividers():
    '''find a natural number in [1, 10000 with a maximum sum of it's dividers'''

    sums = {}
    for i in range(1, 10000):
        sums[i] = 0
    
        for j in range(1, i + 1):
            if i % j == 0:
                sums[i] += j
    
    return max(sums, key=sums.get)

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
                print("A number with a maximum sum of dividers in [1, 10000]", max_sum_dividers())
            else:
                continue

        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


def task_322_menu():
    represent_function(max_sum_dividers, max_sum_dividers.__doc__)


if __name__ == '__task_322_menu__':
    task_322_menu()
