from django.shortcuts import render
from tasks.models import TodoItem, Category

def todo_list(request):
    items = TodoItem.objects.all()
    categories = Category.objects.all()
    context = {"items" : items, "categories" : categories}
    return render(request, "tasks/tasks_list.html", context=context)

def todo_detail(request, pk):
    item = TodoItem.objects.get(pk=pk)
    context = {"item" : item}
    return render(request, "tasks/task_detail.html", context=context)