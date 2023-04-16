from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponse
from django.template import loader
from .models import Collections
# Create your views here.

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
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

    form = UserLoginForm()

    return render(
        request=request,
        template_name = "login.html",
        context={"Form": form}
    )


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

def Profile(request, id):

    context = {

    }

    template = loader.get_template("Profile.html")

    return HttpResponse(template.render(context, request))

def KoleksiyonlarDetay(request, id):
    k = Collections.objects.get(id = id)

    context = {
        "Koleksiyon":k
    }

    template = loader.get_template("CollectionDetails.html")

    return HttpResponse(template.render(context, request))

@login_required
def saved(request):
    User = request.user

    context = {
        "Kaydedilenler": User.bookmarks.all()
    }

    template = loader.get_template("saved.html")

    return HttpResponse(template.render(context, request))

@login_required
def custom_logout(request):
    logout(request)
    return redirect("/")

@login_required
def Koleksiyonlar(request):
    User = request.user
    k = Collections.objects.all().filter(owner = User)

    j = False
    if not k :
        j = True

    context = {
        "Koleksiyon":k,
        "isNull":j
    }

    template = loader.get_template("Collections.html")

    return HttpResponse(template.render(context, request))