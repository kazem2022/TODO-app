from django.contrib import admin

from tasks.models import Category, TodoItem

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "completed"]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)  # Assuming there is an 'author' field in your Task model



admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Category)
