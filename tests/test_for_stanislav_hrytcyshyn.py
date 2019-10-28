import sys
import unittest
sys.path.append('../')

from tasks.task178 import find_multiples
from tasks.task178 import find_squares_of_even_numbers
from tasks.task554 import find_all_pythagorean_triple

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_multiples([1, 3, 6, 9, 15]), 3)
        self.assertEqual(find_multiples([1, 3, 6, 15, 7, 9]), 3)
        self.assertEqual(
            find_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 5)

    def test_case_2(self):
        self.assertEqual(find_squares_of_even_numbers([0, 5, 16, 36, 64, 100]), 5)
        self.assertEqual(find_squares_of_even_numbers([0, 4, 16, 36, 64, 100]), 6)

    def test_case_3(self):
        self.assertTrue((3, 4, 5) in find_all_pythagorean_triple(20))
        self.assertTrue(all(
            [checking in find_all_pythagorean_triple(20) for checking in [(3, 4, 5), (4, 0, 4), (4, 3, 5)]]))


if __name__ == '__main__':
    unittest.main()
