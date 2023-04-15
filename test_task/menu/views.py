from django.shortcuts import render


def index(request, pk=None):
    context = {}
    return render(request, 'menu/index.html', context)
