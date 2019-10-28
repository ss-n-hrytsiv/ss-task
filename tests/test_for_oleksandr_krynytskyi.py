import sys
sys.path.append('../')

from tasks.task88vg import swap_digit, write_digit
from tasks.task332 import lagrange




import unittest


class TestTasks(unittest.TestCase):
    def test_values(self):
        # test write_digit function
        self.assertEqual(write_digit('24'), '1241')
        self.assertEqual(write_digit('444'), '14441')
        self.assertEqual(write_digit('1'), '111')
        self.assertEqual(write_digit('23'), '1231')
        self.assertEqual(write_digit(f'{1 + 23 + 24}'), '1481')

        # test swap_digit function
        self.assertEqual(swap_digit(2345), 5342)
        self.assertEqual(swap_digit(11), 11)
        self.assertEqual(swap_digit(515), 515)
        self.assertEqual(swap_digit(1), 1)

        # test lagrange function
        self.assertEqual(lagrange(11), [3, 1, 1, 0])
        self.assertEqual(lagrange(12), [3, 1, 1, 1])
        self.assertEqual(lagrange(15), [3, 2, 1, 1])
        self.assertEqual(lagrange(1), [1, 0, 0, 0])
    
    def test_types(self):
        # Test if values are incorrect

        self.assertRaises(TypeError, swap_digit, 'any string')
        self.assertRaises(TypeError, swap_digit, None)
        self.assertRaises(TypeError, swap_digit, False)
        self.assertRaises(TypeError, swap_digit, {})
        self.assertRaises(TypeError, swap_digit, ' 1 0')

        self.assertRaises(TypeError, write_digit, 123)
        self.assertRaises(TypeError, write_digit, {})
        self.assertRaises(TypeError, write_digit, None)

        self.assertRaises(ValueError, lagrange, -20)
        self.assertRaises(ValueError, lagrange, -1)
        self.assertRaises(ValueError, lagrange, 0)