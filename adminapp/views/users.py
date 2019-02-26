from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from authapp.models import CustomUser
from adminapp.models.user import UserEdit
# from basketapp.models import Basket

def index(request:HttpRequest):
    users = CustomUser.objects.all()
    return render(request, 'adminapp/users/index.html', {'users': users})

def create(request:HttpRequest):
    return HttpResponse('create')

def read(request:HttpRequest,id):
    user = CustomUser.objects.get(id=id)
    # basket = Basket.objects.get(user=id)
    return render(request, 'adminapp/users/read.html', {'user': user,})

def update(request:HttpRequest,id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        update_form = UserEdit(request.POST, instance=user)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        update_form = UserEdit(instance=request.user)
    content = {
        'user': user,
        'update_form': update_form,
    }
    return render(request, 'adminapp/users/update.html', content)

def delete(request:HttpRequest,id):
    user = CustomUser.objects.get (id=id)
    user.delete()
    return HttpResponseRedirect(reverse('adminapp:users'))
