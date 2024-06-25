from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("groups", views.groups, name="groups"),
    path("tasks", views.tasks, name="tasks"),
]