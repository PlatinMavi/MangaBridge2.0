from django.db import models

# Create your models here.

class Manga(models.Model):
    manga_name = models.CharField(max_length= 255, default="null")
    manga_image = models.ImageField(upload_to="thumbnail", default="thumbnail/noimage.png")
    manga_views= models.IntegerField(default=0)
    manga_description = models.TextField()

    def __str__(self):
        return f"{self.id}, {self.manga_name}"
        

class Fansub(models.Model):
    fansub_name = models.CharField(max_length=255, default="null")

    def __str__(self):
        return f"{self.id}, {self.fansub_name}"

class Chapter(models.Model):
    chapter_number = models.IntegerField(default=0)
    chapter_url = models.URLField(default="www.example.com")
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    fansub = models.ForeignKey(Fansub, on_delete= models.CASCADE)
    relase_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chapter_number}, {self.manga}, {self.fansub}"
    
class Duyuru(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)


class Categorys(models.Model):
    Category_name = models.CharField(max_length=255)
class MangaCategory(models.Model):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)