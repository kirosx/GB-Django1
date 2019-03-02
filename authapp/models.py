from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
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

class CustomUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W'),
    )

    user = models.OneToOneField(CustomUser, unique=True,null=False,db_index=True,on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='tags',max_length=128,blank=True)
    about_me = models.TextField(verbose_name='about',max_length=512, blank=True)
    gender = models.CharField(verbose_name='sex', max_length=1,choices=GENDER_CHOICES,blank=True)

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            CustomUserProfile.objects.create(user=instance)

    @receiver(post_save, sender= CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.customuserprofile.save()

# Create your models here.
