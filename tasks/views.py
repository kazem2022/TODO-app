from django.shortcuts import render
from tasks.models import TodoItem, Category
from tasks.forms import TaskForm
from django.http import HttpResponseRedirect

def todo_list(request):
    items = TodoItem.objects.all()
    categories = Category.objects.all()
    context = {"items" : items, "categories" : categories}
    return render(request, "tasks/tasks_list.html", context=context)

def todo_detail(request, pk):
    item = TodoItem.objects.get(pk=pk)
    context = {"item" : item}
    return render(request, "tasks/task_detail.html", context=context)

def todo_create(request):
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            TodoItem.objects.create(**forms.cleaned_data)
            return HttpResponseRedirect('/tasks/')
    else:
        forms = TaskForm()
    
    return render(request, 'tasks/task_create.html', {'forms' : forms})
    # return render(request, 'tasks/task_create.html', {'forms': forms})
    