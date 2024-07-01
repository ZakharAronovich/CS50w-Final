from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Teacher, Student, Course, Task
from .forms import RegistrationForm, TaskCreationForm
from .decorators import authenticated_only, unauthenticated_only, teachers_only, students_only


def index(request):
    return render(request, "index.html")


@teachers_only
def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "courses.html", context)


@authenticated_only
def tasks(request):
    if request.user.role == "TC":
        teacher = Teacher.objects.get(user=request.user)
        courses = Course.objects.filter(teacher=teacher)
    elif request.user.role == "ST":
        student = Student.objects.get(user=request.user)
        courses = student.courses.all()
    
    tasks = Task.objects.filter(course__in=courses)
    context = {"tasks": tasks}
    return render(request, "tasks.html", context)


@students_only
def courses(request):
    courses = Course.objects.all()
    student = Student.objects.get(user=request.user)
    context = {"courses": courses, "student": student}
    return render(request, "courses.html", context)


@students_only
def enrollment(request, course_id):
    student = Student.objects.get(user=request.user)
    course = Course.objects.get(pk=course_id)
   
    if course in student.courses.all():
        student.courses.remove(course)
    else:
        student.courses.add(course)
    
    student.save()
    return render(request, "courses.html")


@teachers_only
def newtask(request):
    form = TaskCreationForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.instance.teacher = Teacher.objects.get(user=request.user)
        form.save()
        return render(request, "tasks.html", context)
    
    context = {"form": form}
    return render(request, "newtask.html", context)


@authenticated_only
def hub(request):
    if request.user.role == "TC":
        pass
    elif request.user.role == "ST":
        pass
    return render(request, "hub.html")


@unauthenticated_only
def register(request):
    form = RegistrationForm(request.POST or None)
    
    if request.method == "POST":

        # Passwords do not match
        if request.POST["password1"] != request.POST["password2"]:
            context = {"form": form, "message": "Passwords must match."}
            return render(request, "register.html", context)
        
        # Form is filled out correctly
        elif form.is_valid():
            form.save()

            # Creating new user
            user = authenticate(
                username=request.POST["username"], 
                password=request.POST["password1"]
            )
            user.role = request.POST["role"]
            user.save()
            
            # Creating a role-based model
            if user.role == "TC":
                teacher = Teacher()
                teacher.user = user
                teacher.save()
            elif user.role == "ST":
                student = Student()
                student.user = user
                student.save()

            login(request, user)
            return redirect("index")
        
    context = {"form": form}
    return render(request, "register.html", context)


@unauthenticated_only
def login_view(request):
    form = AuthenticationForm(request.POST or None)

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], 
            password=request.POST["password"]
        )

        # Attempt to log the user in
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            context = {"message": "User does not exist.", "form": form}
            return render(request, "login.html", context)
    
    context = {"form": form}
    return render(request, "login.html", context)


@authenticated_only
def logout_view(request):
    logout(request)
    return redirect("index")