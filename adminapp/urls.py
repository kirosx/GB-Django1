from django.urls import path
from adminapp.views import users, products, categories
from adminapp.controllers import users as ctr
from adminapp.controllers.products import StuffUpdateView
app_name = 'adminapp'

urlpatterns = [
    path('users/index', ctr.UserListView.as_view(), name='users'),
    # path('users/index', users.index, name='users'),
    path('users/create', ctr.UserCreateView.as_view(), name='users_create'),
    # path('users/create', users.create, name='users_create'),
    # path('users/read/<int:id>', ctr.UserListView.as_view(), name='users_read'),
    path('users/read/<int:id>', users.read, name='users_read'),
    path('users/update/<int:id>', users.update, name='users_update'),
    path('users/delete/<int:id>', users.delete, name='users_delete'),
    path('categories/index', categories.index, name='categories'),
    path('categories/create', categories.create, name='categories_create'),
    path('categories/read/<int:id>', categories.read,name='categories_read'),
    path('categories/update/<int:id>', categories.update,name='categories_update'),
    path('categories/delete/<int:id>', categories.delete,name='categories_delete'),
    path('products/index', products.index, name='products'),
    path('products/create', products.create, name='products_create'),
    path('products/read/<int:id>', products.read, name='products_read'),
    path('products/update/<int:pk>', StuffUpdateView.as_view(), name='products_update'),
    # path('products/update/<int:id>', products.update, name='products_update'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),
    path('products/list/<int:category>', products.list_by_category, name='products_category'),




]