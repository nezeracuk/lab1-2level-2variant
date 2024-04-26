from src.binary_tree_priority_queue import BinaryTree
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_number_add(self):
        self.tree.add(10, 10)
        self.assertEqual(self.tree.root.priority, 10)
        self.tree.add(8, 8)
        self.assertEqual(self.tree.root.left.priority, 8)
        self.tree.add(12, 12)
        self.assertEqual(self.tree.root.right.priority, 12)
        self.tree.add(9, 11)
        self.assertEqual(self.tree.root.right.left.priority, 11)

    def test_number_pop(self):
        self.tree.add(10, 10)
        self.tree.add(8, 8)
        self.tree.add(12, 12)
        self.tree.add(11, 11)
        self.tree.add(9, 9)
        self.tree.add(20, 20)
        self.tree.add(5, 5)
        self.assertEqual(self.tree.pop(), 20)

if __name__ == '__main__':
    unittest.main()