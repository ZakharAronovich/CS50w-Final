from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("TC", "Teacher"),
        ("ST", "Student"),
    )

    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=None, null=True)


class Teacher(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="teacher_by_user"
    )


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="student_by_user"
    )
    teachers = models.ManyToManyField(Teacher, related_name="students")


class Task(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, 
        related_name="created_tasks", default=None
    )
    students = models.ManyToManyField(Student, related_name="assigned_tasks")
    datetime = models.DateTimeField(auto_now_add=True)
    due_to = models.DateTimeField()
    text = models.TextField(max_length=1024)