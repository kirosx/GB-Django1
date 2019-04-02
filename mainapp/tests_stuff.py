from django.test import TestCase
from mainapp.models import Stuff, Category


class ProductsTestCase(TestCase):
    def setUp(self):
        category = Stuff.objects.create(name='Chairs')
        self.product1 = Stuff.objects.create(name='Chair#1', category=category, price=100,quantity=200)
        self.product2 = Stuff.objects.create(name='Chair#2', category=category, price=1000,quantity=220)
        self.product3 = Stuff.objects.create(name='Chair#3', category=category, price=10000,quantity=222)

    def test_product_get(self):
        product1 = Stuff.objects.get(name='Chair#1')
        product2 = Stuff.objects.get(name='Chair#2')
        product3 = Stuff.objects.get(name='Chair#3')
        self.assertEqual(product1, self.product1)
        self.assertEqual(product2, self.product2)
        self.assertEqual(product3, self.product3)

    def test_product_get_items(self):
        product1 = Stuff.objects.get(name='Chair#1')
        product3 = Stuff.objects.get(name='Chair#3')
        products = product1.get_items()
        self.assertEqual(list(products), [product1,product3])

