from django.shortcuts import render, HttpResponseRedirect

from django.http import HttpRequest, HttpResponse
from authapp.forms import LoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse

def login(request:HttpRequest):
    title = 'войти'
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=login, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    content = {
        'title':title,
        'login_form':login_form,
    }
    return render(request, 'authapp/login.html', content)

def logout(request:HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect ('/')

def redirect_to_login(request:HttpRequest):
    return HttpResponseRedirect('/auth/login')

def register(request:HttpRequest):
    title ='register'
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        reg_form = RegisterForm()
    content = {
        'title': title,
        'reg_form': reg_form,
    }
    return render(request, 'authapp/register.html', content)


def edit(request:HttpRequest):
    title ='Edit'
    if request.method == 'POST':
        update_form = UpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = UpdateForm(instance=request.user)
    content = {
        'title': title,
        'update_form': update_form,
    }
    return render(request, 'authapp/edit.html', content)