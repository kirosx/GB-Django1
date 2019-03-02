from django.core.management.base import BaseCommand
from authapp.models import CustomUser, CustomUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = CustomUser.objects.all()
        for user in users:
            users_profile = CustomUserProfile.objects.create(user=user)
            users_profile.save()