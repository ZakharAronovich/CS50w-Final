from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    assigned_to = models.ManyToManyField(User, related_name="assigned_tasks")
    datetime = models.DateTimeField(auto_now_add=True)
    due_to = models.DateTimeField()
    text = models.TextField(max_length=1024)