from django.contrib import admin
from .models import CustomUser, Collections, Comments
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Collections)
admin.site.register(Comments)