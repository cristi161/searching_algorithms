from algorithms.Node import Node


class Tree:
    def __init__(self):
        self.root = Node(1)

        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)
        node10 = Node(10)

        self.root.left = node2
        self.root.right = node3

        node2.left = node4
        node2.right = node5
        node5.left = node6
        node5.right = node7
        node3.left = node8
        node3.right = node9
        node9.right = node10

    def get_nodes(self):
        nodes = list()
        self.root.dfs_nodes(nodes)

        return nodes


if __name__ == "__main__":
    pass
