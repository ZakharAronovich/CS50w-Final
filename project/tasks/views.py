from django.shortcuts import render, redirect
from .models import User, Teacher, Student
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')


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


def logout_view(request):
    logout(request)
    return redirect("index")
