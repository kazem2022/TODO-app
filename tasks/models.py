from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.title
