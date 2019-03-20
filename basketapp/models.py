from django.db import models
from mainapp.models import Stuff
from django.conf import settings


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args,**kwargs)


class Basket(models.Model):
    _price: float
    _total_qty: int
    _total_price: float

    objects = BasketQuerySet.as_manager()

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
    
    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')
    
    @staticmethod
    def get_product(user,product):
        return Basket.objects.filter(user=user, product=product)
    
    @classmethod
    def get_product_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]
        return basket_items_dic
    
    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args,**kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()








