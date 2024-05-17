import unittest
from src.wchain import find_the_longest_chain, read_file_from_input, result_file

class TestFindTheLongestChain(unittest.TestCase):
    def test_case1(self):
        words = read_file_from_input('src/resources/input_from_file.txt')
        result = find_the_longest_chain(words)
        result_file('src/resources/output_from_file.txt', result)
        self.assertEqual(result, 6)

    def test_case2(self):
        words = read_file_from_input('src/resources/input_from_file2.txt')
        result = find_the_longest_chain(words)
        result_file('src/resources/output_from_file2.txt', result)
        self.assertEqual(result, 4)

    def test_case3(self):
        words = read_file_from_input('src/resources/input_from_file3.txt')
        result = find_the_longest_chain(words)
        result_file('src/resources/output_from_file3.txt', result)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
