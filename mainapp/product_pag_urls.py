from django.urls import path
import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.products, name='index'),
    path('<int:page>/', controller.products, name='page'),
]