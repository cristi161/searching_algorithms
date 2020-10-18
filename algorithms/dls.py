def get_graph():
    return {'Oradea': ['Zerind', 'Sibiu'],
         'Zerind': ['Arad', 'Oradea'],
         'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
         'Timisoara': ['Lugoj', 'Arad'],
         'Lugoj': ['Mehedia', 'Timisoara'],
         'Mehedia': ['Lugoj', 'Dobreta'],
         'Dobreta': ['Mehedia', 'Craiova'],
         'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
         'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Craiova'],
         'Bucharest': ['Pitesti', 'Giurgiu', 'Fagaras', 'Urziceni'],
         'Fagaras': ['Sibiu', 'Bucharest'],
         'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Arad', 'Oradea'],
         'Rimnicu Vilcea': ['Pitesti', 'Sibiu', 'Craiova'],
         'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
         'Neamt': ['Issl'],
         'Issl': ['Neamt', 'Vaslui'],
         'Vaslui': ['Issl', 'Urziceni'],
         'Hirsova': ['Urziceni', 'Eforie'],
         'Giurgiu': ['Bucharest'],
         'Eforie': ['Hirsova']
         }

route = []
visited = []

graph = get_graph()

def dls(start, destination):
    lmt = 10

    route.append(start)
    countnode = 0
    countlimit = 0
    nodeinlevel = 0

    while len(route) > 0:
        vertex = route.pop(len(route) - 1)
        if vertex not in visited:
            visited.append(vertex)
            route.extend(set(graph[vertex]) - set(visited))
            countnode += 1
        if nodeinlevel == countnode:
            nodeinlevel = len(route)
            countnode = 0
            countlimit += 1
        if countlimit == lmt:
            print('cut off')
            break
        if visited.__contains__(destination):
            return visited


if __name__ == "__main__":
    v = dls("Arad", "Bucharest")

    print(v)
