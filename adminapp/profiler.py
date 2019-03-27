from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import connection
from mainapp.models import Category



def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x:type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}:')
    [print(query['sql']) for query in update_queries]


@receiver(pre_save, sender=Category)
def stuff_is_active_category_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)

        db_profile_by_type(sender, 'UPDATE', connection.queries)
