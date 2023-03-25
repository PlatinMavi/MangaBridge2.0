from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import CustomUser
from django.contrib.auth import get_user_model, login
from .forms import UserRegistrationForm
# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save
            login(request , user)
            return redirect("/")
        
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    context={
        "Form":form
    }

    template = loader.get_template("registration.html")
    return HttpResponse(template.render(request, context))
