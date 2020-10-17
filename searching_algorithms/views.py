from django.contrib.sites import requests
from django.shortcuts import render

from algorithms.bfs import Graph
from algorithms.dfs import Tree
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

    context = {'nodes': nodes}
    return render(request, 'bfs.html', context)


def dijkstra_page(request):
    context = {}
    return render(request, 'dijkstra.html', context);

def min_max_page(request):
    context = {}
    return render(request, 'min_max.html', context);
