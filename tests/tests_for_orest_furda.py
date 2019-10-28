import unittest
from tasks.task_87 import task_87
from tasks.task_226 import task_226
from tasks.task_559 import task_559


class TestAlgorithmTaskFunctions(unittest.TestCase):

    def test_task_87(self):
        self.assertEqual(task_87([1, 2, 3, 4, 5, 6, 7], 4), 22)
        self.assertEqual(task_87([6, 7, 5, 8], 2), 13)
        self.assertEqual(task_87([2, 3, 4, 5, 1], 5), 15)

    def test_task_226(self):
        self.assertEqual(task_226(12, 20), [60, 120, 180, 240])
        self.assertEqual(task_226(4, 7), [28])
        self.assertEqual(task_226(9, 21), [63, 126, 189])

    def test_task_559(self):
        self.assertEqual(task_559(786), [1, 3, 7, 15, 31, 63, 127, 255, 511])
        self.assertEqual(task_559(47), [1, 3, 7, 15, 31])
        self.assertEqual(task_559(127), [1, 3, 7, 15, 31, 63])


if __name__ == '__main__':
    unittest.main()