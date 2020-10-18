class Dijkstra:
    def __init__(self, graph: dict):
        self.graph = graph
        self.max_int = 9999999

    def dijkstra(self, src, dst):
        shortest_dist = {}  # final path
        predecessor = {}
        unvisited = self.graph
        path = []

        for node in unvisited:
            shortest_dist[node] = self.max_int

        shortest_dist[src] = 0

        while unvisited:
            min_node = None
            for node in unvisited:
                if min_node is None:
                    min_node = node
                elif shortest_dist[node] < shortest_dist[min_node]:
                    min_node = node

            for child_node, weight in self.graph[min_node].items():
                if weight + shortest_dist[min_node] < shortest_dist[child_node]:
                    shortest_dist[child_node] = weight + shortest_dist[min_node]
                    predecessor[child_node] = min_node
            unvisited.pop(min_node)

        current_node = dst
        while current_node != src:
            try:
                path.insert(0, current_node)
                current_node = predecessor[current_node]
            except KeyError:
                print("Key not reachable")
                break
        if shortest_dist != self.max_int:
            print("Shortest dist: ", str(shortest_dist[dst]))
            print("And the path: ", str(path))


if __name__ == "__main__":
    d = Dijkstra({'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}})
    d.dijkstra('a', 'd')