from django.db import models

from django.conf import settings
from mainapp.models import Stuff

class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING,'Order is forming'),
        (SENT_TO_PROCEED,'Order is proceeding'),
        (PROCEEDED,'Order proceeded'),
        (PAID,'Order is payed'),
        (READY,'Order is ready'),
        (CANCEL,'Cancelled order'),

    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated', auto_now=True)
    status = models.CharField(verbose_name='status',max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='activity', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Current Order:{self.id}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Stuff, verbose_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity-=self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args,**kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__,self).delete()
