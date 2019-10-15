import math


def get_elements_by_condition():
    """
    Count how many integer numbers satisfy the condition 2^k < Ak < k!.
    :param sequence: some sequence of integer number.
    :return: count of numbers.
    """
    print("Input some number sequence of numbers by \' \':")
    try:
        sequence = [int(number) for number in input().split(' ')]
    except Exception:
        print('Input error. Try again!')
        sequence = []
    elements_and_indexes = {sequence[i]: i + 1
                            for i in range(1, len(sequence) - 1)}
    filtered_values = filter(lambda element:
                             2 ** element[1] < element[0] < math.factorial(element[1]),
                             elements_and_indexes.items())
    return len(dict(filtered_values))
