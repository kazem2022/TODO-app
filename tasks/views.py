from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasks.forms import TaskForm, TaskCategoryForm
from tasks.models import Category, TodoItem


@login_required
def todo_list(request):
    items = TodoItem.objects.all()
    categories = Category.objects.all()
    context = {"items": items, "categories": categories}
    return render(request, "tasks/tasks_list.html", context=context)


@login_required
def todo_detail(request, pk):
    item = TodoItem.objects.get(pk=pk)
    context = {"item": item}
    return render(request, "tasks/task_detail.html", context=context)


@login_required
def todo_create(request):
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            TodoItem.objects.create(**forms.cleaned_data)
            return HttpResponseRedirect("/tasks/")
    else:
        forms = TaskForm()

    return render(request, "tasks/task_create.html", {"forms": forms})

@login_required
def category_create(request):
    if request.method == "POST":
        forms = TaskCategoryForm(request.POST)
        if forms.is_valid():
            Category.objects.create(**forms.cleaned_data)
            return HttpResponseRedirect("/tasks/")
    else:
        forms = TaskCategoryForm()

    return render(request, "tasks/category_create.html", {"forms": forms})
