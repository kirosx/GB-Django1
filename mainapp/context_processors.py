from basketapp.models import Basket
from django.http import HttpRequest


def basket(request:HttpRequest):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return {
        'basket':basket
    }