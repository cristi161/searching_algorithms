from algorithms.Node.BFSNode import BFSNode


class Graph:
    def __init__(self, root=BFSNode(1)):
        self.root = root
        self.generate_nodes()

    def generate_nodes(self):
        self.root.add_node(BFSNode(2))
        self.root.add_node(BFSNode(3))
        self.root.add_node(BFSNode(4))

        node2 = self.root.nodes[0]
        node2.add_node(BFSNode(5))
        node2.add_node(BFSNode(6))

        node3 = self.root.nodes[1]
        node3.add_node(BFSNode(7))

        node4 = self.root.nodes[2]
        node4.add_node(BFSNode(8))
        node4.add_node(BFSNode(9))

        node7 = node3.nodes[0]
        node7.add_node(BFSNode(10))
        node7.add_node(BFSNode(11))
        node7.add_node(BFSNode(12))
        node7.add_node(BFSNode(13))

    def BFS(self, nodes_: list):
        queue = list()
        queue.append(self.root)

        while queue:
            s = queue.pop(0)
            nodes_.append(s.value)

            for node in s.nodes:
                queue.append(node)


if __name__ == "__main__":
    graph = Graph(root=BFSNode(1))
    nodes = []

    graph.BFS(nodes)

    print(nodes)