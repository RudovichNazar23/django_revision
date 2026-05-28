from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import LoginUserForm


@csrf_exempt
def welcome_page(request):
    if request.method == "GET":
        return render(request, "user_app/welcome_page.html", {
            "create_form": UserCreationForm,
        })
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username, password = request.POST["username"], request.POST["password1"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
            return redirect("main_page")

        return render(request, "user_app/welcome_page.html", {"create_form": form})


@csrf_exempt
def login_user(request):
    if request.method == "GET":
        return render(request, "user_app/login.html", {"form": LoginUserForm})
    else:
        form = LoginUserForm(request.POST)

        username, password = request.POST["username"], request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main_page")
        form.add_error("", "Wrong credentials")
        return render(request, "user_app/login.html", {"form": form})


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("welcome_page")


@csrf_exempt
def main_page(request):
    if request.method == "GET":
        return render(request, "user_app/main_page.html", {"request": request})
