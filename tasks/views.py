from django.shortcuts import render
from tasks.models import TodoItem, Category

def todo_list(request):
    items = TodoItem.objects.all()
    context = {"items" : items}
    return render(request, "tasks/index.html", context=context)
