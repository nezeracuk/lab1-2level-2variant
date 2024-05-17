import unittest
from src.detect_cycle import Graph, read_graph, output


class TestCycleDetection(unittest.TestCase):
    def test_cycle_detection(self):
        graph_object = Graph(read_graph('src/resources/input.txt'))
        with open('src/resources/output.txt', 'r') as file:
            output_content = file.read()
        self.assertEqual(output_content, 'True')

if __name__ == '__main__':
    unittest.main()
