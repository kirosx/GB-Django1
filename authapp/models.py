from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    ava = models.ImageField(upload_to='avatars', verbose_name='аватар',)
    email = models.EmailField(verbose_name='email', blank='True')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expired = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() >= self.activation_key_expired:
            return True
        return False

# Create your models here.
