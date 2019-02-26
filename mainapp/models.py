from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=30)

class Stuff(models.Model):
    name = models.CharField(verbose_name='Бренд', max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='stuff', verbose_name='logo')
    description = models.TextField(verbose_name='Description',blank=True)
    price = models.DecimalField(verbose_name='price',max_digits=10, decimal_places=2)
# Create your models here.
