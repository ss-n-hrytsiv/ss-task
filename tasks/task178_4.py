"""
178(4).
Given n natural numbers: A1, ..., An.
Determine which members of ​​the sequence (Ak)
satisfying the condition Ak < (Ak-1 + Ak+1) / 2.
"""
__author__ = 'Valentyn Malenchak'

def get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor(sequence):
    """
    Count how many integer numbers satisfy the condition
    Ak < (Ak-1 + Ak+1) / 2.
    :param sequence: some sequence of integer numbers.
    :return: count of numbers.
    """
    arithmetic_means_for_elements = {sequence[i]:
                                     (sequence[i-1] + sequence[i+1]) / 2
                                     for i in range(1, len(sequence) - 1)}
    filtered_values = filter(lambda element: element[0] < element[1],
                             arithmetic_means_for_elements.items())
    return len(dict(filtered_values))


def task_178_4_menu():
    print('-' * 100)
    print(f'Function logic:\n{get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor.__doc__}')
    print('-' * 50)
    print("Input some sequence of integer numbers by \' \':\n")
    try:
        sequence = [int(number) for number in input().split(' ')]
        print(f'Result: {get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor(sequence)}')
    except Exception as error:
        print(f'{error}. Try again!'.title())


if __name__ == '__main__':
    task_178_4_menu()
