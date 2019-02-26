from django.db import models
from mainapp.models import Stuff
from django.conf import settings


class Basket(models.Model):
    _price: float
    _total_qty: int
    _total_price: float

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)
    add_datetime = models.DateTimeField(verbose_name='data', auto_now_add=True)

    @property
    def product_price(self):
        return self.product.price * self.quantity

    @property
    def total_qty(self):
        items = Basket.objects.filter(user=self.user)
        total = sum([x.quantity for x in items])
        return total

    @property
    def total_price(self):
        items = Basket.objects.filter(user=self.user)
        total = sum([x.product_price for x in items])
        return total








