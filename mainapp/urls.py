from django.urls import path
import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.product, name='index'),
    path('<int:id>/', controller.product, name='category'),
    path('cat<int:id>/', controller.category, name='cat'),
]