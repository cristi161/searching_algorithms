graph = {
    'a': ['b', 'c', [5, 2]],
    'b': ['a', 'd', 'g', [5, 5, 1]],
    'c': ['a', 'f', 'g', [2, 5, 4]],
    'd': ['b', [5]],
    'e': ['b', [1]],
    'f': ['c', [5]],
    'g': ['g', [4]],
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

    src = str('a')
    dst = str('f')
    v = ucs(src, dst)

    print("The Shortest Path from " + src + " To " + dst + ":  ")

    print(v)
