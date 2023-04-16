from django.urls import path

from. import views

urlpatterns = [
    path("Register/", views.Register, name="Register"),
    path("Login/", views.custom_login, name="custom_login"),
    path("Logout/", views.custom_logout, name="custom_logout"),
    path("Profile/<int:id>/", views.Profile, name="profile"),
    path("Saved/", views.saved, name="saved"),
    path("Collections/", views.Koleksiyonlar, name="koleksiyonlar"),
    path("Collections/<int:id>/", views.KoleksiyonlarDetay, name="koleksiyonlardetay")
]