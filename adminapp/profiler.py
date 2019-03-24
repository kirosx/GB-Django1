from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import connection



def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x:type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}:')
    [print(query['sql']) for query in update_queries]

    