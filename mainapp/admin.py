from django.contrib import admin
from .models import Category, Stuff
from authapp.models import CustomUser

# Register your models here.
admin.site.register(Category)
admin.site.register(Stuff)
admin.site.register(CustomUser)