class Graph:
    def __init__(self,neighbors):
        self.graph = neighbors

    def detect_cycle(self,start_node):
        visited = set()
        queue = [(start_node,None)]

        while queue:
            current_node,parent = queue.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor,current_node))
                elif neighbor != parent:
                    return True
        return False

def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            node, neighbors = line.strip().split(':')
            neighbors_list = neighbors.strip('[] \n').split(',')
            graph[node.strip()] = [n.strip() for n in neighbors_list if n]
    return graph

def output(file_path, result):
    with open(file_path,'w') as file:
        file.write(str(result))

graph = read_graph('../src/resources/input.txt')
main_graph = Graph(graph)
cycle_detected = any(main_graph.detect_cycle(node) for node in graph)
output_file_path = '../src/resources/output.txt'
output(output_file_path, cycle_detected)
