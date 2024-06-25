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


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="student_by_user"
    )


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Group(models.Model):
    title = models.CharField(max_length=128, default=None)
    students = models.ManyToManyField(Student, related_name="groups_by_student")


    def __str__(self):
        return self.title


class Task(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, 
        related_name="created_tasks", default=None
    )
    groups = models.ManyToManyField(Group)
    datetime = models.DateTimeField(auto_now_add=True)
    due_to = models.DateTimeField()
    text = models.TextField(max_length=1024)