import unittest
from tasks.task178_4 import get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor
from tasks.task178_5 import get_count_of_elements_by_condition
from tasks.task555 import get_pascal_triangle


class SSTest(unittest.TestCase):
    """Unit test for ss-v-malenchak
    """

    def test_task178_4(self):
        self.assertEqual(get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor(
            [2, 6, 9, 8, 5, 4, 7, 8, 5, 3, 6, 5, 5]), 3)
        self.assertEqual(get_count_of_elements_less_than_arithmetic_mean_of_its_neighbor(
            [75, 99, 34, 12, 126, 78]), 2)

    def test_task178_5(self):
        self.assertEqual(get_count_of_elements_by_condition(
            [88, 65, 68, 71, 58, 72, 84, 59, 46, 86, 75, 94, 81, 3, 56]), 2)
        self.assertEqual(get_count_of_elements_by_condition(
            [15, 38, 13, 40, 77, 5, 51, 92, 58, 34, 50, 49, 75, 86, 22]), 1)

    def test_task555(self):
        self.assertEqual(get_pascal_triangle(1), '1')
        self.assertEqual(get_pascal_triangle(3), '1\n1 1\n1 2 1')


if __name__ == "__main__":
    unittest.main()
