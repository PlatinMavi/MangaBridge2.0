from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Manga, Chapter, Fansub, Duyuru, Categorys, SSS
from django.core.paginator import Paginator
from Users.models import CustomUser, Comments
from django.urls import reverse
from .forms import CommentForm
# Create your views here.
def Index(request):
    manga = Manga.objects.all()
    chapter = Chapter.objects.all().order_by("manga_id" ,"-relase_date").distinct("manga_id")[:20]
    fansub = Fansub.objects.all().values()
    duyuru = Duyuru.objects.all()

    duyuru_len = len(duyuru)
    duyuru = duyuru[duyuru_len-1]

    mostview = manga.order_by("-manga_views")[:5]

    context={
        "Manga": manga,
        "Chapter": chapter,
        "Fansub": fansub,
        "MostView": mostview,
        "Duyuru": duyuru,
    }

    template = loader.get_template("Index.html")

    return HttpResponse(template.render(context, request))

def MangaView(request, id):
    manga = Manga.objects.get(id = id)
    chapter = Chapter.objects.filter(manga = id)
    chapter_ = chapter.order_by("fansub","chapter_number")
    available_fansubs = list(set([o.fansub for o in chapter]))
    categorys = manga.manga_categorys.all()
    comments = Comments.objects.all().filter(manga=id)

    manga.manga_views = manga.manga_views+1
    manga.save()

    bolsay = chapter.order_by("-chapter_number")[0].chapter_number
    
    issaved= False
    
    if request.user.is_authenticated:
        User = request.user
        cu = CustomUser.objects.get(username=User)
        ubm = cu.bookmarks.filter(id = id).exists()
        if ubm == True:
            issaved = True
        else:
            issaved = False

    if request.method == "POST":
        User = request.user
        txt = request.POST.get("content")
        if len(txt) > 2 :
            o = Comments.objects.create(comment = txt, owner = User, manga = manga)
            o.save()
            return HttpResponseRedirect(reverse("MangaView", args=[id])) 
        else:
            print("hatatatatatatata")

    context={
        "Manga": manga,
        "Chapter": chapter_,
        "Fansub": available_fansubs,
        "BolumSayi": bolsay,
        "Categorys": categorys,
        "IsSaved":  issaved,
        "Comments": comments,
    }

    template = loader.get_template("MangaView.html")

    return HttpResponse(template.render(context, request))

def NewUploads(request):
    chapter = Chapter.objects.all().order_by("-relase_date")
    paginator = Paginator(chapter, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        "Chapter":page_obj
    }

    template = loader.get_template("NewUploads.html")

    return HttpResponse(template.render(context, request))

def DuyuruView(request):
    duyuru = Duyuru.objects.all().order_by("-id")

    context = {
        "Duyuru":duyuru
    }

    template = loader.get_template("Duyuru.html")

    return HttpResponse(template.render(context, request))

def Archive(request):
    filte = request.GET.get("category")
    manga = Manga.objects.all()
    if filte != None:
        manga = manga.filter(manga_categorys=filte)

    cats = Categorys.objects.all()
    paginator = Paginator(manga, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    manlen = len(manga)
    
    context = {
        "Category": cats,
        "Manga": page_obj,
        "MangaLen":manlen,
    }

    template = loader.get_template("Category.html")

    return HttpResponse(template.render(context, request))

def Search(request):
    search = request.GET.get("Search")
    mangaresults = Manga.objects.all()

    if search != None:
        mangaresults = mangaresults.filter(manga_name__icontains=search)

    paginator = Paginator(mangaresults, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    manlen = len(mangaresults)

    context = {
        "Manga":page_obj,
        "MangaLen":manlen,
    }

    template = loader.get_template("Search.html")

    return HttpResponse(template.render(context, request))

def QnA(request):
    q = SSS.objects.all()

    context = {
        "SSS":q
    }

    template = loader.get_template("SSS.html")

    return HttpResponse(template.render(context, request))

def SaveManga(request, id):
    User = request.user
    manga = Manga.objects.get(id = id)
    cu = CustomUser.objects.get(username=User)
    if cu.bookmarks.filter(id = id).exists():
        cu.bookmarks.remove(manga)

    else :
        cu.bookmarks.add(manga)

    return HttpResponseRedirect(reverse("MangaView", args=[id])) 
