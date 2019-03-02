from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest,HttpResponseRedirect, JsonResponse
from mainapp.models import Stuff
from basketapp.models import Basket


def add(request: HttpRequest, id : int):
    product = get_object_or_404(Stuff, pk=id)
    exist_item = Basket.objects.filter(product__id=id)
    if exist_item:
        exist_item[0].quantity += 1
        exist_item[0].save()
    else:
        new_item = Basket(user=request.user,product=product)
        new_item.quantity = 1
        new_item.save()

    if request.is_ajax():
        return JsonResponse({
            'quantity':Basket.objects.get(product__id=id).quantity,
        })

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove(request: HttpRequest, id: int):
    item = Basket.objects.get(product__id=id)
    item.quantity -= 1
    item.save()

    if request.is_ajax():
        return JsonResponse({
            'quantity':Basket.objects.get(product__id=id).quantity,
        })

    return HttpResponseRedirect (request.META['HTTP_REFERER'])


def index(request:HttpRequest):
    products = Basket.objects.filter(user=request.user)
    context = {'products': products, 'total': products[0].total_price if products else ''}
    return render(request, 'basketapp/index.html', context)

