from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from tasks.forms import TaskForm, TaskCategoryForm
from tasks.models import Category, TodoItem

@login_required
def todo_list(request):
    categories = Category.objects.filter(user=request.user)
    user_tasks = {}

    for cat in categories:
        user_tasks[cat] = cat.todoitem_set.filter(user=request.user)

    context = {
        'categories': categories,
        'user_tasks': user_tasks
    }
    return render(request, "tasks/tasks_list.html", context=context)

@login_required
def todo_detail(request, pk):
    item = get_object_or_404(TodoItem, user=request.user, pk=pk)
    
    context = {"item": item}
    return render(request, "tasks/task_detail.html", context=context)


@login_required
def todo_create(request):
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():

            TodoItem.objects.create(**forms.cleaned_data, user=request.user)
            return HttpResponseRedirect("/tasks/")
    else:
        forms = TaskForm()

    return render(request, "tasks/task_create.html", {"forms": forms})

@login_required
def category_create(request):
    if request.method == "POST":
        forms = TaskCategoryForm(request.POST)
        if forms.is_valid():
            Category.objects.create(**forms.cleaned_data, user=request.user)
            return HttpResponseRedirect("/tasks/")
    else:
        forms = TaskCategoryForm()

    return render(request, "tasks/category_create.html", {"forms": forms})
