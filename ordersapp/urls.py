import ordersapp.views as controller
from django.urls import path

app_name = 'ordersapp'

urlpatterns = [
    path('',controller.OrderList.as_view(), name='order_list'),
]