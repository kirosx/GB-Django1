from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from authapp.models import CustomUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy


class UserListView(ListView):
    model = CustomUser
    template_name = 'adminapp/users/index.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'adminapp/users/update.html'
    fields = ('__all__')
    success_url = reverse_lazy('adminapp:users')


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'adminapp/users/update.html'
    fields = ('__all__')
    success_url = reverse_lazy('adminapp:users')

    def get_context_data(self, **kwargs):
        parent_context = super(UserUpdateView, self).get_context_data(**kwargs)
        return parent_context