import unittest
import sys
sys.path.append('../')
from unittest.mock import patch
from tasks.task_86_a_b import task_86_a
from tasks.task_86_a_b import task_86_b
from tasks.task_330 import task330


class Test(unittest.TestCase):
    def test_task86_a(self):
            expected_answer = 2
            expected_input = 10
            actual_answer = task_86_a(expected_input)
            self.assertEqual(actual_answer, expected_answer)

    def test_task86_b(self):
        expected_answer = 15
        expected_input = 12345
        actual_answer = task_86_b(expected_input)
        self.assertEqual(actual_answer, expected_answer)

    def test_task330(self):
        expected_answer = [0, 6]
        expected_input = 10
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task330(), expected_answer)


if __name__ == '__main__':
    unittest.main()
