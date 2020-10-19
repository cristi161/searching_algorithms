class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        print(self.data)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def dfs_nodes(self, data: list):
        data.append(self.data)
        if self.left:
            self.left.dfs_nodes(data)
        if self.right:
            self.right.dfs_nodes(data)