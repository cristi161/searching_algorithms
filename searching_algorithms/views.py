from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from algorithms import dfs
from algorithms.dfs import Tree
import json


def index_page(request):
    tree = Tree()

    nodes = tree.get_nodes()
    JSONData = json.dumps(nodes)
    print(JSONData)

    context = {'nodes': JSONData}
    return render(request, 'index.html', context)
