from django.urls import path

from. import views

urlpatterns = [ 
    path("", views.Index, name = "Index"),
    path("Details/<int:id>", views.MangaView, name= "MangaView"),
    path("NewUpload/", views.NewUploads, name="NewUploads"),
    path("Duyuru/", views.DuyuruView, name="duyuru"),
    path("Details/<int:id>/Save", views.SaveManga, name="save"),
    path("Archive/", views.Archive, name="archive"),
    path("Search/", views.Search, name="search"),
    path("SSS/", views.QnA, name="SSS"),
]