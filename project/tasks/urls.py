from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("courses", views.courses, name="courses"),
    path("tasks", views.tasks, name="tasks"),
    path("courses", views.courses, name="courses"),
    path("enrollment/<int:course_id>", views.enrollment, name="enrollment"),
    path("newtask", views.newtask, name="newtask"),
    path("hub", views.hub, name="hub"),
]