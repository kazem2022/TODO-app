from django.contrib import admin

from tasks.models import Category, TodoItem

# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "completed"]


admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Category)
