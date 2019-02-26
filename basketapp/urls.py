from django.urls import path
import basketapp.views as controller


app_name = 'basketapp'

urlpatterns = [
    path('', controller.index, name='index'),
    path('add/<int:id>/', controller.add, name='add'),
    path('remove/<int:id>/', controller.remove, name='remove'),
]