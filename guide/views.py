from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'guide/index.html', {'title1': 'Weekly planning', 'title2': 'Shopping list', 'title3': 'Personal settings'})

