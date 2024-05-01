import unittest
from src.sum_of_depths import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_balanced_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        self.assertEqual(sum_of_depths(root), 10)

if __name__ == '__main__':
    unittest.main()
