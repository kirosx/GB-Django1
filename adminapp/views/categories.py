from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from mainapp.models import Category, Stuff
from adminapp.models.category import CategoryEdit


@user_passes_test(lambda u: u.is_superuser)
def index(request:HttpRequest):
    category = Category.objects.all()
    return render(request, 'adminapp/categories/index.html', {'category': category})


@user_passes_test(lambda u: u.is_superuser)
def create(request:HttpRequest):
    return HttpResponse('create')


@user_passes_test(lambda u: u.is_superuser)
def read(request:HttpRequest,id):
    title = Category.objects.get(pk=id)
    cat_stuff = Stuff.objects.filter(category__id=id)
    return render(request, 'adminapp/categories/read.html', {'category': cat_stuff,'title':title})


@user_passes_test(lambda u: u.is_superuser)
def update(request:HttpRequest,id):
    title = Category.objects.get(pk=id)
    if request.method == 'POST':
        update_form = CategoryEdit(request.POST, instance=title)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        update_form = CategoryEdit(instance=request.user)
    content = {
        'title': title,
        'update_form': update_form,
    }
    return render(request,'adminapp/categories/update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def delete(request:HttpRequest,id):
    title = Category.objects.get(pk=id)
    title.delete()
    return HttpResponseRedirect(reverse('adminapp:categories'))
