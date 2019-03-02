from django.shortcuts import render, HttpResponseRedirect

from django.http import HttpRequest, HttpResponse
from authapp.forms import LoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse
from authapp.models import CustomUser
from django.core.mail import send_mail
from geekshop import settings
from django.db import transaction
from authapp.forms import CustomUserProfileEditForm


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
            user = reg_form.save()
            if send_verify_mail(user):
                print('Confirmation sended')
                return HttpResponseRedirect(reverse('auth:login'))
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        reg_form = RegisterForm()
    content = {
        'title': title,
        'reg_form': reg_form,
    }
    return render(request, 'authapp/register.html', content)

@transaction.atomic
def edit(request:HttpRequest):
    title ='Edit'
    if request.method == 'POST':
        update_form = UpdateForm(request.POST,request.FILES, instance=request.user)
        profile_form = CustomUserProfileEditForm(request.POST,instance=request.user.customuserprofile)
        if update_form.is_valid() and profile_form.is_valid() :
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = CustomUserProfileEditForm(instance=request.user.customuserprofile)
    content = {
        'title': title,
        'update_form': update_form,
        'profile_form':profile_form
    }
    return render(request, 'authapp/edit.html', content)


def verify(request:HttpRequest,email,activation_key):
    try:
        user = CustomUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request,'authapp/verify.html')
        else:
            print(f'ERROR {user}')
            return render(request, 'authapp/verify.html')
    except Exception as e:
        print(f'error {e.args}')
        return HttpResponseRedirect(reverse('home'))


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    title = f'Confirmation {user.email}'
    message = f'For confirmation {user.username} account, please follow \n {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)