class Graph:
    def __init__(self, nodes=None):
        """
        Ініціалізація графа.
        Args:
        nodes (list, optional): Список вузлів для додавання у граф спочатку.
        """
        self.edges = []
        self.nodes = set(nodes) if nodes else set()

    def add_edge(self, start, end, weight):
        """
        Додає ребро до графа з вказаними вагою і вузлами.

        Args:
        start (str): Початковий вузол ребра.
        end (str): Кінцевий вузол ребра.
        weight (int): Вага ребра.
        """
        self.edges.append((weight, start, end))
        self.nodes.update([start, end])

    def find_parent(self, parent, node):
        """
        Рекурсивний пошук кореневого вузла для даного вузла.

        Args:
        parent (dict): Словник батьківських відносин між вузлами.
        node (str): Вузол, для якого потрібно знайти кореневий вузол.

        Returns:
        Кореневий вузол для заданого вузла.
        """
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def kruskal_mst(self):
        """
        Реалізація алгоритму Крускала для знаходження мінімального остовного дерева графа.

        Returns:
        Вага кістякового дерева або -1, якщо створення MST неможливе.
        """
        if not self.edges:
            return -1

        #Сортуємо ребра за вагою для подальшої обробки у порядку зростання.
        self.edges.sort()

        #Ініціалізація батьків кожного вузла, початково вузол є батьком самому собі.
        parent = {node: node for node in self.nodes}

        #Ініціалізуємо загальну вагу остовного дерева та лічильник включених ребер.
        total_weight = 0
        mst_edges = 0

        #Обробка кожного ребра за порядком ваги.
        for weight, start, end in self.edges:
            #Знаходимо кореневі вузли для поточних вузлів ребра.
            root_start = self.find_parent(parent, start)
            root_end = self.find_parent(parent, end)

            #Якщо кореневі вузли різні, ребро не утворює циклу.
            if root_start != root_end:
                total_weight += weight  #Додаємо вагу ребра до загальної ваги MST.
                mst_edges += 1  #Збільшуємо кількість ребер у MST.
                parent[root_start] = root_end  #Об'єднуємо дві компоненти зв'язності.

        #Перевіряємо, чи всі вузли з'єднані. Якщо так, повертаємо загальну вагу, якщо ні - повертаємо -1.

        #Перевірка, чи всі вузли з'єднані
        if mst_edges == len(self.nodes) - 1:
            return total_weight
        else:
            return -1

def read_input_file(min_cable_path):
    """
    Зчитування даних ребер з файлу CSV.

    Args:
    min_cable_len (str): Шлях до файлу CSV.

    Returns:
    Початковий вузол, кінцевий вузол, вага.
    """
    edges = []
    with open(min_cable_path, "r") as file:
        for line in file:
            parts = line.split(',')
            edges.append((parts[0], parts[1], int(parts[2])))
    return edges
