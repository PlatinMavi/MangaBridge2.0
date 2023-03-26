from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "registration.html",
        context={"Form": form}
    )

@login_required

def custom_logout(request):
    logout(request)
    return redirect("/")

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username= form.cleaned_data["username"],
                password= form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return(redirect("/"))
        else:
            for error in list(form.errors.values()):
                print(request, error)

    form = AuthenticationForm()

    return render(
        request=request,
        template_name = "login.html",
        context={"Form": form}
    )