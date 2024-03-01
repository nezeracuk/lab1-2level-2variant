import unittest
from Second_Lab import monotony

class Test_Second_Lab(unittest.TestCase):
    def test_Monotony(self):
        self.assertEqual(monotony([3,5,6,7,3,2,5,7,5]), False)
        self.assertEqual(monotony([1,2,3,4,5]),True)
        self.assertEqual(monotony([5,5,5,5,5,5]),True)
        self.assertEqual(monotony([]),True)


if __name__ == '__main__':
    unittest.main()
