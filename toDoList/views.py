from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
from django.views.decorators.http import require_POST

# main Page render


def index(request):
    todo_items = ToDoList.objects.order_by('id')
    form = ToDoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'toDoList/index.html', context)

# Adding new item to Database


@require_POST
def addToDoItem(request):
    form = ToDoListForm(request.POST)

    if form.is_valid():
        new_todo = ToDoList(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

# Making item completed


def completedToDo(request, todo_id):
    todo = ToDoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

# deleting the completed items


def deleteCompleted(request):
    ToDoList.objects.filter(completed__exact=True).delete()
    return redirect('index')

# delete everything


def deleteAll(request):
    ToDoList.objects.all().delete()
    return redirect('index')
