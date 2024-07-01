from django.shortcuts import redirect


def authenticated_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def unauthenticated_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def teachers_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif request.user.role != "TC":
            return redirect("index")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def students_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        elif request.user.role != "ST":
            return redirect("index")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper