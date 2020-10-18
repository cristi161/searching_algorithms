graph = {
    'A': ['B', 'C', [5, 2]],
    'B': ['A', 'D', 'E', [5, 5, 1]],
    'C': ['A', 'F', 'G', [2, 5, 4]],
    'D': ['B', [5]],
    'E': ['B', [1]],
    'F': ['C', [5]],
    'G': ['G', [4]],
}

route = []
visited = []
sortedWeight = []
sortedPoint = []

def ucs(start, destination):
    route.append(start)
    while len(route) > 0:
        vertex = route.pop(0)
        if vertex not in visited:
            visited.append(vertex)

            sortedWeight = sorted(graph[vertex][len(graph[vertex]) - 1])

            for i in sortedWeight:
                sortedPoint.append(graph[vertex][graph[vertex][len(graph[vertex]) - 1].index(i)])

            route.extend(set(sortedPoint) - set(visited))
        if visited.__contains__(destination):
            break
    return route


if __name__ == "__main__":

    suru = str('A')
    ses = str('F')
    v = ucs(suru, ses)

    print("The Shortest Path from " + suru + " To " + ses + ":  ")

    print(v)
