from django.core.management.base import BaseCommand
from mainapp.models import Category, Stuff
from django.db import connection
from django.db.models import Q, F, When, Case, DecimalField, IntegerField
from datetime import timedelta
from adminapp.profiler import db_profile_by_type

class Command(BaseCommand):
    def handle(self, *args, **options):
        test_products = Stuff.objects.filter(
            Q(category__name='Lanterns') |
            Q(category__name='Bowls')
        )

        print(len(test_products))
        db_profile_by_type('learn_db', '', connection.queries)
