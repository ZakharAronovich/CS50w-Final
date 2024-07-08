from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timesince
from django.core.exceptions import ValidationError


class User(AbstractUser):
    ROLE_CHOICES = (
        ("TC", "Teacher"),
        ("ST", "Student"),
    )

    image = models.ImageField(null=True, blank=True, upload_to="images/")
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=None, null=True)
    bio = models.TextField(max_length=256, blank=True, null=True)


    @property 
    def member_for(self):
        return timesince.timesince(self.date_joined)


class Teacher(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        default=None, related_name="teacher_by_user"
    )


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Tag(models.Model):
    TAG_CHOICES = (
        ("ALG", "Algebra"),
        ("ART", "Art"),
        ("BIO", "Biology"),
        ("CHE", "Chemistry"),
        ("ENG", "English"),
        ("GEO", "Geography"),
        ("HIS", "History"),
        ("PE", "PE")
    )

    name = models.CharField(max_length=3, choices=TAG_CHOICES)


    def __str__(self):
        return f"{self.name} Tag"


class Course(models.Model):
    title = models.CharField(max_length=50, default=None, null=True)
    image = models.ImageField(default=None,blank=True, null=True, upload_to="images/")
    description = models.TextField(max_length=512, default=None, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, 
        related_name="courses_by_teacher"
    )
    tags = models.ManyToManyField(Tag, related_name="courses_by_tag")


    def __str__(self):
        return self.title


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
    deadline = models.DateTimeField()
    text = models.TextField(max_length=1024)

    @property
    def time_left(self):
        value = str(timesince.timeuntil(self.deadline))
        try:
            return f"{value[:value.index(",")]} left"
        except:
            return f"{value} left"