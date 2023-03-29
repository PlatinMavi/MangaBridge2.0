from django.db import models
from django.contrib.auth.models import AbstractUser
from Manga.models import Manga
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=1000, null=True)
    profile_picture = models.ImageField(upload_to="pp", default="thumbnail/noimage.png")

    bookmarks = models.ManyToManyField(Manga, null=True)
    def __str__(self):
        return self.username
    
class Collections(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=512)
    content = models.ManyToManyField(Manga)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

