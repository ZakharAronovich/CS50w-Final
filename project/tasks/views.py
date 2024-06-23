from django.shortcuts import render, redirect
from .models import User, Teacher, Student
from .forms import UserForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')


def register(request):
    form = UserForm(request.POST or None)
    
    if request.method == "POST":

        # Passwords do not match
        if request.POST["password1"] != request.POST["password2"]:
            context = {"form": form, "message": "Passwords must match."}
            return render(request, "register.html", context)
        
        # Form is filled out correctly
        elif form.is_valid():

            # Creating new user
            user = authenticate(
                username=request.POST["username"], 
                password=request.POST["password1"]
            )
            user.role = request.POST["role"]
            user.save()
            
            # Creating a role-based model
            if user.role == "TC":
                teacher = Teacher(user)
                teacher.save()
            elif user.role == "ST":
                student = Student(user)
                student.save()

            login(request, user)
            return redirect("index")
        
    context = {"form": form}
    return render(request, "register.html", context)