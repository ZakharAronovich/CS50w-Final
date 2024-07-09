from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("courses", views.courses, name="courses"),
    path("tasks", views.tasks, name="tasks"),
    path("courses/<int:tag_id>", views.courses, name="courses"),
    path("enrollment/<int:course_id>", views.enrollment, name="enrollment"),
    path("create/<str:entry_type>", views.create, name="create"),
    path("course/<int:course_id>", views.course, name="course"),
    path("profile/<int:user_id>", views.profile, name="profile"),
]