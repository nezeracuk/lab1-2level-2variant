import unittest
from src.kmp import kmp

class TestKMPAlgorithm(unittest.TestCase):
    def test_single_occurrence(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(kmp(haystack, needle), [6])

    def test_multiple_occurrences(self):
        haystack = "ababcabcabababd"
        needle = "ababd"
        self.assertEqual(kmp(haystack, needle), [10])

    def test_no_occurrence(self):
        haystack = "abcde"
        needle = "xyz"
        self.assertEqual(kmp(haystack, needle), "Not found")

    def test_needle_longer_than_haystack(self):
        haystack = "short"
        needle = "longerthanshort"
        self.assertEqual(kmp(haystack, needle), "Haystack can't be longer than needle")

    def test_empty_needle(self):
        haystack = "text"
        needle = ""
        self.assertEqual(kmp(haystack, needle), "You must find something to search for")

    def test_empty_haystack(self):
        haystack = ""
        needle = "text"
        self.assertEqual(kmp(haystack, needle), "Not found")

    def test_needle_and_haystack_are_empty(self):
        haystack = ""
        needle = ""
        self.assertEqual(kmp(haystack, needle), "You must find something to search for")

    def test_needle_equals_haystack(self):
        haystack = "exact"
        needle = "exact"
        self.assertEqual(kmp(haystack, needle), [0])

    def test_case_sensitivity(self):
        haystack = "Hello World"
        needle = "world"
        self.assertEqual(kmp(haystack, needle), "Not found")


if __name__ == "__main__":
    unittest.main()
