import unittest

from src.min_size_of_board import min_board_size

class Test_min_size_of_board(unittest.TestCase):
    def test_lab2(self):
        self.assertEqual(min_board_size(10, 2, 3), 9)
        self.assertEqual(min_board_size(2, 1000000000, 999999999), 1999999998)
        self.assertEqual(min_board_size(4, 1, 1), 2)


if __name__ == '__main__':
    unittest.main()
