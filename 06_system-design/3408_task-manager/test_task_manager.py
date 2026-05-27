import unittest

from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            [1, 101, 5],
            [2, 102, 3],
            [3, 103, 4]
        ]
        self.tm = TaskManager(self.tasks)

    def test_initial_execTop(self):
        self.assertEqual(self.tm.execTop(), 1)  # Task 101 with priority 5

    def test_add_and_execTop(self):
        self.tm.add(4, 104, 6)
        self.assertEqual(self.tm.execTop(), 4)  # Task 104 with priority 6

    def test_edit_and_execTop(self):
        self.tm.edit(102, 7)  # Change task 102 priority to 7
        self.assertEqual(self.tm.execTop(), 2)  # Task 102 with priority 7

    def test_rmv_and_execTop(self):
        self.tm.rmv(101)  # Remove task 101
        self.assertEqual(self.tm.execTop(), 3)  # Task 103 with priority 4

    def test_multiple_operations(self):
        self.tm.add(5, 105, 2)
        self.tm.edit(103, 8)
        self.assertEqual(self.tm.execTop(), 3)  # Task 103 with priority 8
        self.tm.rmv(103)
        self.assertEqual(self.tm.execTop(), 1)  # Task 102 with priority 3
        self.tm.rmv(102)
        self.assertEqual(self.tm.execTop(), 5)  # Task 105 with priority 2
        self.tm.rmv(105)
        self.assertEqual(self.tm.execTop(), -1) # No tasks left

    def test_execTop_empty(self):
        self.tm.rmv(101)
        self.tm.rmv(102)
        self.tm.rmv(103)
        self.assertEqual(self.tm.execTop(), -1)  # No tasks left