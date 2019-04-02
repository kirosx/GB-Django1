from django.views.generic import UpdateView
from django.forms import ModelForm
from mainapp.models import Category
from django.urls import reverse_lazy
from adminapp.models.category import CategoryEdit
from django.db.models import F
from django.db import connection
from adminapp.profiler import db_profile_by_type


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'adminapp/categories/update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = CategoryEdit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(price=F('price')*(1-discount/100))
                db_profile_by_type(self.__class__,'UPDATE',connection.queries)
        return super().form_valid(form)
