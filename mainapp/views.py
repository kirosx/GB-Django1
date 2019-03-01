from typing import Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
import datetime
from .models import Category, Stuff
from basketapp.models import Basket
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.
links_menu = [
{'href': 'home', 'name': 'Home'},
{'href': 'products:index', 'name': 'Products'},

{'href': 'contact', 'name': 'Contact'},
]


def index(request):
    intro = Stuff.objects.all ()[:4]
    trending = Stuff.objects.all ()[8:15]
    return render(request,'mainapp/index.html', {'links': links_menu,'intro':intro, 'trending':trending})

def products(request:HttpRequest, page=1):
    category = Category.objects.all()
    stuff = Stuff.objects.all()
    provider = Paginator(stuff, 3)
    try:
        product_provider = provider.page(page)
    except PageNotAnInteger:
        product_provider = provider.page(1)
    except EmptyPage:
        product_provider = provider.page(provider.num_pages)
    return render(request,'mainapp/products.html', {'provider': product_provider, 'men': category, 'stuff':stuff})

def contact(request):
    return render(request,'mainapp/contact.html', {'links': links_menu,'men': category})

def product(request:HttpRequest,id=None):
    category = Category.objects.all()
    if not id:
        return render (request, 'mainapp/product.html', {'links': links_menu, 'men': category,})
    else:
        product = Stuff.objects.get(id=id)
        same = Stuff.objects.exclude(pk=id).filter(category=product.category)
        return render(request, 'mainapp/product.html', {'links': links_menu, 'men': category,'product':product,'same': same,})

def category(request:HttpRequest,id=None):
    get_object_or_404(Category,pk=id)
    cat = Stuff.objects.filter(category=id)
    return render(request, 'mainapp/cat.html', {'cat': cat, 'men': category,})



def test(request):
    date = {'today': str(datetime.date.today())}
    return render(request, 'mainapp/child.html', date)