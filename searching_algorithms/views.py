import math

from django.contrib.sites import requests
from django.shortcuts import render

from algorithms.bfs import Graph
from algorithms.dfs import Tree
from algorithms.dijsktra import Dijkstra
import json

from algorithms.dls import dls, get_graph
from algorithms.minmax import minimax
from algorithms.puzzle import Puzzle
from algorithms.ucs import ucs


def index_page(request):
    tree = Tree()

    nodes = tree.get_nodes()
    JSONData = json.dumps(nodes)
    print(JSONData)

    context = {'nodes': JSONData}
    return render(request, 'index.html', context)


def bfs_page(request):
    BFSGraph = Graph()

    nodes = list()
    BFSGraph.BFS(nodes)
    JSONData = json.dumps(nodes)

    context = {'nodes': JSONData}
    return render(request, 'bfs.html', context)


def dijkstra_page(request):
    d = Dijkstra({'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}})
    d.dijkstra('a', 'd')

    path = d.get_full_path()
    JSONData = json.dumps(path)

    print(JSONData)

    context = {'nodes': JSONData}
    return render(request, 'dijkstra.html', context)

def min_max_page(request):
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    treeDepth = math.log(len(scores), 2)
    result = minimax(0, 0, True, scores, treeDepth)

    JSONDataScores = json.dumps(scores)

    context = {'scores': JSONDataScores, 'depth': treeDepth, 'result': result}
    return render(request, 'min_max.html', context)

def ucs_page(request):

    JSONDataPath = json.dumps(ucs("a", "f"))

    context = {'path': JSONDataPath}
    return render(request, 'ucs.html', context)

def puzzle_page(request):
    p = Puzzle((0, 0), (3, 6))
    path = []

    JSONDataGraph = json.dumps(p.puzzle)
    p.go(path)
    JSONDataPath = json.dumps(path)

    context = {'path': JSONDataPath, 'graph': JSONDataGraph}
    return render(request, 'puzzle.html', context)

def dls_page(request):
    path = dls("Arad", "Bucharest")

    graph = get_graph()
    JSONGraph = json.dumps(graph)

    context = {'graph': str(JSONGraph), 'path': str(json.dumps(path))}
    return render(request, 'dls.html', context)


