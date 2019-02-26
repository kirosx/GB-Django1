from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authapp.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        CustomUser.objects.create_superuser('root', 'my@nl.com', '123123', age=30)