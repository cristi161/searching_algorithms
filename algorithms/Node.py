class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.data)

    def dfs_nodes(self, data: list):
        if self.left:
            self.left.dfs_nodes(data)
        if self.right:
            self.right.dfs_nodes(data)
        data.append(self.data)