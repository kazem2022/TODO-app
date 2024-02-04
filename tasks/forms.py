from datetime import datetime

from django import forms

from tasks.models import Category, TodoItem


class TaskForm(forms.Form):
    # title = forms.CharField(max_length=100)
    # detail = forms.CharField(widget=forms.Textarea)
    # created_date = forms.DateTimeInput(widget=forms.DateTimeField)
    # completed = forms.BooleanField(default=False)
    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    title = forms.CharField(max_length=100)
    detail = forms.CharField(widget=forms.Textarea)
    created_date = forms.DateTimeField(initial=datetime.now)
    completede = forms.BooleanField(required=False)
    # category = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class TaskCategoryForm(forms.Form):
    name = forms.CharField(max_length=100)
    
