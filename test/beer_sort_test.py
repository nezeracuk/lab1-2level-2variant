import unittest
from src.beer_sort import minimum_types_of_beer

class TestBeerSelection(unittest.TestCase):
    def test_two_preferences(self):
        result = minimum_types_of_beer(2, 2, ["YN", "NY"])
        self.assertEqual(result, 2)

    def test_same_beer(self):
        result = minimum_types_of_beer(3, 2, ["YN", "YN", "YN"])
        self.assertEqual(result, 1)

    def test_no_preferences(self):
        result = minimum_types_of_beer(2, 2, ["NN", "NN"])
        self.assertEqual(result, 0)

    def test_somebody_without_preferences(self):
        result = minimum_types_of_beer(3, 2, ["NN", "YY", "NY"])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

