class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
        else:
            self.priority_add(self.root, new_node)

    def priority_add(self, current_node, new_node):
        if current_node.priority <= new_node.priority:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.priority_add(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.priority_add(current_node.left, new_node)

    def pop(self):
        parent = None
        current = self.root

        if not self.root:
            return None

        while current.right:
            parent = current
            current = current.right
        if parent:
            parent.right = current.left
        else:
            self.root = current.left
        return current.priority



    def search(self):
        if not self.root:
            return None
        node = self.root
        while node.right.right:
            node = node.right
        return node, node.right

    def check_tree(self, node):
        if node is None:
            return

        self.check_tree(node.right)
        print(node.priority)
        self.check_tree(node.left)