from django.urls import path
import mainapp.views as controller
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', cache_page(360)(controller.products), name='index'),
    path('<int:page>/', controller.products, name='page'),
]