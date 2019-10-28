import unittest
from tasks.task_num_107 import task_num_107
from tasks.task_num_243_a import task_num_243_a
from tasks.task_num_243_b import task_num_243_b


class TestAlgoTasks(unittest.TestCase):

    def test_task107(self):
        expected_answer = 3
        actual_answer = task_num_107(231)
        self.assertEqual(actual_answer, expected_answer)

    def test_task_243_a(self):
        expected_answer = (1, 5)
        actual_answer = task_num_243_a(26)
        self.assertEqual(actual_answer, expected_answer)

    def test_task_243_b(self):
        expected_answer = [(0, 5), (3, 4)]
        actual_answer = task_num_243_b(25)
        self.assertEqual(actual_answer, expected_answer)

if __name__ == '__main__':
    unittest.main()

