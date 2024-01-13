from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_add_now=True)
    completed = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    