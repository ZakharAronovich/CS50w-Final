from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timesince


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


class Group(models.Model):
    title = models.CharField(max_length=128, default=None)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, 
        related_name="groups_by_teacher"
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="student_by_user"
    )
    group = models.ForeignKey(
        Group, on_delete=models.PROTECT,
        related_name="students_by_group",
        blank=True, null=True,
    )


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Task(models.Model):
    SUBJECT_CHOICES = (
        ("ALG", "Algebra"),
        ("ART", "Art"),
        ("BIO", "Biology"),
        ("CHE", "Chemistry"),
        ("ENG", "English"),
        ("GEO", "Geography"),
        ("HIS", "History"),
        ("PE", "PE")
    )

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, 
        related_name="tasks_by_group"
    )
    subject = models.CharField(
        max_length=3, choices=SUBJECT_CHOICES, 
        default=None, null=True,
    )
    datetime = models.DateTimeField(auto_now_add=True)
    due_to = models.DateTimeField()
    text = models.TextField(max_length=1024)


    @property
    def time_left(self):
        value = str(timesince.timeuntil(self.due_to))
        try:
            return f"{value[:value.index(",")]} left"
        except:
            return f"{value} left"