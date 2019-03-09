import ordersapp.views as controller
from django.urls import path

app_name = 'ordersapp'

urlpatterns = [
    path('',controller.OrderList.as_view(), name='order_list'),
    path('formingcomplete/<id:int>',controller.order_forming_complete, name='order_forming_complete'),
    path('create/',controller.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<id:int>', controller.OrderRead.as_view(),name='order_read'),
    path('update/<id:int>', controller.OrderItemsUpdate.as_view(),name='order_update'),
    path('delete/<id:int>', controller.OrderDelete.as_view(),name='order_delete'),
]