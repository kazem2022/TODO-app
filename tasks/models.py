from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    