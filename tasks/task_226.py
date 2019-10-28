# 226
# Given are natural n, m. Get all their natural common multiples, smaller mn.
__author__ = 'Orest Furda'


def task_226(first_number, second_number):
    """Given are natural n, m. Get all their natural common multiples, smaller mn."""

    product_of_numbers = first_number * second_number
    common_multiples_for_the_first_number = [i for i in range(
        1, product_of_numbers + 1) if i % first_number == 0]
    common_multiples_for_the_second_number = [i for i in range(1, product_of_numbers + 1)
                                              if i % second_number == 0]

    common_multiples_for_the_both_numbers = sorted(list(set(
        common_multiples_for_the_first_number) & set(common_multiples_for_the_second_number)))

    return common_multiples_for_the_both_numbers


def task_226_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_226.__doc__)
        print('-' * 50)
        print('-' * 100)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)
        print('\n\n\n')

        user_input_first_number = input('Please input a first number(n): ')

        if user_input_first_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break

        user_input_second_number = input('Please input a second number(m): ')

        try:
            first_number = int(user_input_first_number)
            second_number = int(user_input_second_number)
            common_multiples_for_the_both_numbers = task_226(
                first_number, second_number)
            print(
                f'Common multiples for {first_number} and {second_number}, less then {first_number * second_number} = {common_multiples_for_the_both_numbers}')
            print('\n\n\n')
        except ValueError:
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_226_menu()
