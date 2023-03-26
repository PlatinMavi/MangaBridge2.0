from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=1000)
    profile_picture = models.ImageField(upload_to="pp", default="thumbnail/noimage.png")

    def __str__(self):
        return self.username
    
