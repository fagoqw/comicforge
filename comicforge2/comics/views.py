from django.shortcuts import render, redirect
from .models import Comic, Panel
from django.contrib.auth.decorators import login_required


def home(request, comic=None):
    if request.method == 'POST':
        return render(request, 'home.html', {'comic': comic})
    else:
        return render(request, 'home.html', {'comic': comic})


def comics_create(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        return render(request, 'create.html', {'comic': comic})
    else:
        return render(request, 'create.html', {'comic': comic})


def comic_detail(request, pk):
    comic = Comic.objects.get(pk=pk)
    return render(request, 'detail.html', {'comic': comic})


@login_required
def panel_add(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        pass
    else:
        pass


@login_required
def panel_edit(request, pk, panel_pk):
    comic = Comic.objects.get(pk=pk)
    panel = Panel.objects.get(pk=panel_pk)
    if request.method == 'POST':
        pass
    else:
        pass


def panel_delete(request, pk, panel_pk):
    comic = Comic.objects.get
