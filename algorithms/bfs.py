from algorithms.Node.BFSNode import BFSNode


class Graph:
    def __init__(self, root: BFSNode):
        self.root = root

    def generate_nodes(self):
        self.root.add_vertice(BFSNode(2))
        self.root.add_vertice(BFSNode(3))
        self.root.add_vertice(BFSNode(4))

        node2 = self.root.vertices[0]

        node2.add_vertice(BFSNode(5))
        node2.add_vertice(BFSNode(6))

graph = Graph(root = BFSNode(1))

graph.generate_nodes()