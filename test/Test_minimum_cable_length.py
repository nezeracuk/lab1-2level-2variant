import unittest
from src.minimum_cable_length import Graph, read_input_file

class TestGraphFunctionality(unittest.TestCase):
    def load_graph_from_file(self, file_path):
        """
        Бере файл CSV, який містить дані про ребра та повертає граф

        Юзаємо read_input_file,щоб прочитати дані з csv файлу,
        ініціалізує граф з вузлами, отриманими з цих ребер, та додає ребра до графа.

        file_path = Шлях до CSV файлу, який містить дані про ребра.
        Формат файлу повинен бути start/end/weight, де
        start та end = вузли, weight= вага,
        в нашому випадку відстань між колодязями.
        """
        edges = read_input_file(file_path)
        nodes = set()
        graph = Graph(nodes=list(nodes))
        for start, end, weight in edges:
            graph.nodes.update([start, end])
            graph.add_edge(start, end, weight)
        return graph

    def test_default_case(self):
        """
        Тестування звичайного випадку мст
        :return:
        """
        graph = self.load_graph_from_file('../src/resources/communication_wells3.csv')
        expected_mst_weight = 150
        result = graph.kruskal_mst()
        self.assertEqual(result, expected_mst_weight)

    def test_no_edges(self):
        """
        Тестування відсутності ребер у графі
        """
        graph = self.load_graph_from_file('../src/resources/communication_wells2.csv')
        result = graph.kruskal_mst()
        self.assertEqual(result, -1)

    def test_isolated_nodes(self):
        """
        Тестування наявності незалежних вершин, для цього створюю окремо
        isolated_edges незалежно від інших еджів та додаю умову відокремлених
        вершин, які незалежні від початкової умови.
        """
        isolated_edges = read_input_file('../src/resources/communication_wells4.csv')
        isolated_nodes = set(['K4', 'K5'])
        isolated_graph = Graph(nodes=list(isolated_nodes))
        for start, end, weight in isolated_edges:
            isolated_graph.nodes.update([start, end])
            isolated_graph.add_edge(start, end, weight)
        result = isolated_graph.kruskal_mst()
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
