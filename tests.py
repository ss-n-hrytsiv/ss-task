import unittest

from algo_tasks import task_num_243_b, task_num_243_a, task_num_107
from unittest.mock import patch


class TestAlgoTasks(unittest.TestCase):

    def test_task107(self):
        expected_answer = 3
        expected_input = 232
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task_num_107(), expected_answer)

    def test_task_243_a(self):
        expected_answer = (1, 5)
        expected_input = 26
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task_num_243_a(), expected_answer)

    def test_task_243_b(self):
        expected_answer = [(0, 5), (3, 4)]
        expected_input = 25
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task_num_243_b(), expected_answer)


if __name__ == '__main__':
    unittest.main()

