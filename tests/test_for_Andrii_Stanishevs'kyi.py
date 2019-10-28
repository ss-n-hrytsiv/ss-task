import unittest
from task_108 import task_108
from task_331_a import task_331_a
from task_331_b import task_331_b

class Test_tasks(unittest.TestCase):

    def test_task_108(self):
        self.assertEqual(task_108(2), 4)  
        self.assertEqual(task_108(100), 128)              
        with self.assertRaises(Exception):
            task_108('ssssss')
    def test_task_331_a(self):
        self.assertEqual(task_331_a(3), [1, 1, 1])  
        self.assertEqual(task_331_a(-1), 'n must be bigger than 0')              
        with self.assertRaises(Exception):
            task_331_a('ssssss')

    def test_task_331_b(self):
        self.assertEqual(task_331_b(7), [])  
        self.assertEqual(task_331_b(10), [[0, 1, 3], [0, 3, 1], [1, 0, 3], [1, 3, 0], [3, 0, 1], [3, 1, 0]])              
        with self.assertRaises(Exception):
            task_331_b('ssssss')
       

if __name__=="__main__":
    unittest.main()