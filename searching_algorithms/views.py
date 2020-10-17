from django.contrib.sites import requests
from django.shortcuts import render
from algorithms.dfs import Tree
import json


def index_page(request):
    tree = Tree()

    nodes = tree.get_nodes()
    JSONData = json.dumps(nodes)
    print(JSONData)

    context = {'nodes': JSONData}
    return render(request, 'index.html', context)
