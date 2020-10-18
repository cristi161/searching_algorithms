from django.contrib.sites import requests
from django.shortcuts import render

from algorithms.bfs import Graph
from algorithms.dfs import Tree
from algorithms.dijsktra import Dijkstra
import json


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
    context = {}
    return render(request, 'min_max.html', context)
