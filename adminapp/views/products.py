from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from mainapp.models import Stuff
from adminapp.models.product import ProductEdit

def index(request:HttpRequest):
    models = Stuff.objects.all()
    return render(request,'adminapp/products/index.html', {'models': models})

def create(request:HttpRequest):
    return HttpResponse('create')

def read(request:HttpRequest,id):
    stuff = Stuff.objects.get(id=id)
    category = stuff.category
    return render(request, 'adminapp/products/read.html', {'stuff': stuff,'category':category})

def update(request:HttpRequest,id):
    title = Stuff.objects.get(pk=id)
    if request.method == 'POST':
        update_form = ProductEdit(request.POST, instance=title)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        update_form = ProductEdit(instance=request.user)
    content = {
        'title': title,
        'update_form': update_form,
    }
    return render(request, 'adminapp/categories/update.html', content)

def delete(request:HttpRequest,id):
    title = Stuff.objects.get(pk=id)
    title.delete()
    return HttpResponseRedirect(reverse('adminapp:products'))

def list_by_category(request:HttpRequest,category):
    return HttpResponse('list')
