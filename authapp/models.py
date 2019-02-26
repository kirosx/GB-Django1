from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст')
    ava = models.ImageField(upload_to='avatars', verbose_name='аватар',)

# Create your models here.
