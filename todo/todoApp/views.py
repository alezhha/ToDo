from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from todoApp.models import Todo
from django.shortcuts import render

# Create your views here.

def homepage(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos':todos})

def create(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        todo = Todo.objects.get(id = id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.description = request.POST.get('description')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'todo':todo})
    except Todo.DoesNotExist:
        return HttpResponseNotFound
        ("<h2>Задача не найдена</h2>")