from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timesince
from django.core.exceptions import ValidationError


def deadline_validator(value):
    until_deadline = str(timesince.timeuntil(value))

    # Chosen deadline is in the past
    if until_deadline.startswith("0"):
        raise ValidationError("The deadline must be in the future.")
    

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


class Course(models.Model):
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

    subject = models.CharField(max_length=3, default=None, choices=SUBJECT_CHOICES)
    description = models.TextField(max_length=512, default=None, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, 
        related_name="courses_by_teacher"
    )


    def __str__(self):
        return self.get_subject_display()


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="student_by_user"
    )
    courses = models.ManyToManyField(
        Course,
        related_name="students_by_course",
    )


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Task(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, 
        related_name="tasks_by_course"
    )
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(validators=[deadline_validator])
    text = models.TextField(max_length=1024)


    @property
    def time_left(self):
        value = str(timesince.timeuntil(self.deadline))
        try:
            return f"{value[:value.index(",")]} left"
        except:
            return f"{value} left"