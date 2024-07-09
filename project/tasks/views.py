from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Teacher, Student, Course, Task, Tag
from .forms import RegistrationForm, TaskCreationForm, CourseCreationForm
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


def courses(request, tag_id=None):
    if tag_id:
        courses = Course.objects.filter(tags=tag_id)
        tag = Tag.objects.get(pk=tag_id)
        context = {"courses": courses, "tag": tag}
    else:  
        context = {"courses": Course.objects.all()}

    return render(request, "courses.html", context)


def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    context = {"course": course}
    return render(request, "course.html", context) 


@students_only
def enrollment(request, course_id):
    student = Student.objects.get(user=request.user)
    course = Course.objects.get(pk=course_id)
   
    if course in student.courses.all():
        student.courses.remove(course)
    else:
        student.courses.add(course)
    
    student.save()
    return redirect("hub")


@teachers_only
def create(request, entry_type):

    if entry_type == "course":
        tags = Tag.objects.all()
        form = CourseCreationForm(request.POST or None)
        context = {"form": form, "entry_type": entry_type, "tags": tags}
        
    elif entry_type == "task": 
        form = TaskCreationForm(request.POST or None)
        context = {"form": form, "entry_type": entry_type}
        
    if request.method == "POST" and form.is_valid():
        form.instance.teacher = Teacher.objects.get(user=request.user)
        form.save()
        
        if entry_type == "course":
            return render(request, "courses.html", context)
        elif entry_type == "task":
            return render(request, "tasks.html", context)
    
    return render(request, "create.html", context)


@authenticated_only
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    
    if user.role == "TC":
        teacher = Teacher.objects.get(user=user)
        courses = Course.objects.filter(teacher=teacher)
        context = {"courses": courses}

    elif user.role == "ST":
        student = Student.objects.get(user=user)
        courses = student.courses.all()
        tasks = Task.objects.filter(course__in=courses)
        context = {"courses": courses, "tasks": tasks}
     
    return render(request, "profile.html", context)


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