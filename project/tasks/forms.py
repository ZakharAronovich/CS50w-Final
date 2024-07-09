from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task, Course


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "role"]


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ["course", "deadline", "text"]


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "image", "tags"]