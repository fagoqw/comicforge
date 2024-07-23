from django.shortcuts import render, redirect
from .models import Comic, Panel
from django.contrib.auth.decorators import login_required

# ... (остальные представления)

@login_required
def comic_create(request):
    if request.method == 'POST':
        # ... (обработка формы создания комикса)
    else:
        # ... (отображение формы создания комикса)

@login_required
def comic_edit(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        # ... (обработка формы редактирования комикса)
    else:
        # ... (отображение формы редактирования комикса)

@login_required
def comic_detail(request, pk):
    comic = Comic.objects.get(pk=pk)
    return render(request, 'comics/comic_detail.html', {'comic': comic})

@login_required
def panel_add(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        # ... (обработка формы добавления панели)
    else:
        # ... (отображение формы добавления панели)

@login_required
def panel_edit(request, pk, panel_pk):
    comic = Comic.objects.get(pk=pk)
    panel = Panel.objects.get(pk=panel_pk)
    if request.method == 'POST':
        # ... (обработка формы редактирования панели)
    else:
        # ... (отображение формы редактирования панели)

@login_required
def panel_delete(request, pk, panel_pk):
    comic = Comic.objects.get


from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Черновик'), ('published', 'Опубликовано')])

class Panel(models.Model):
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE)
    order = models.IntegerField()
    image = models.ImageField(upload_to='comics/images')
    text_elements = models.JSONField(default=[])

