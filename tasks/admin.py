# from django.contrib import admin
# from .models import Category, TodoItem

# class TodoItemAdmin(admin.ModelAdmin):
#     list_display = ["title", "created_date", "completed"]
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)  # Assuming there is an 'author' field in your Task model

# class CategoryAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=request.user)  # Filtering based on the user field

#     def save_model(self, request, obj, form, change):
#         if not request.user.is_superuser:
#             obj.user = request.user
#         obj.save()

# admin.site.register(TodoItem, TodoItemAdmin)
# admin.site.register(Category, CategoryAdmin)






# from django.contrib import admin
# from .models import Category, TodoItem

# class TodoItemAdmin(admin.ModelAdmin):
#     list_display = ["title", "created_date", "completed"]
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)

# class CategoryAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=request.user)

#     def save_model(self, request, obj, form, change):
#         if not obj.user:  # Assigning user only if not present
#             obj.user = request.user
#         obj.save()

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields['user'].queryset = form.base_fields['user'].queryset.filter(pk=request.user.pk)
#         return form

# admin.site.register(TodoItem, TodoItemAdmin)
# admin.site.register(Category, CategoryAdmin)




# from django.contrib import admin
# from .models import Category, TodoItem

# class TodoItemAdmin(admin.ModelAdmin):
#     list_display = ["title", "created_date", "completed"]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(category__user=request.user)

# class CategoryAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=request.user)

#     def save_model(self, request, obj, form, change):
#         if not obj.user:  # Assigning user only if not present
#             obj.user = request.user
#         obj.save()

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.base_fields['user'].queryset = form.base_fields['user'].queryset.filter(pk=request.user.pk)
#         return form

# admin.site.register(TodoItem, TodoItemAdmin)
# admin.site.register(Category, CategoryAdmin)




from django.contrib import admin
from .models import Category, TodoItem
from django.contrib.auth.models import User


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "completed"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__user=request.user)

class CategoryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)  # Assuming there is an 'author' field in your Task model

    def save_model(self, request, obj, form, change):
        if not obj.user:  # Assigning user only if not present
            obj.user = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user' and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Category, CategoryAdmin)