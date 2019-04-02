from django.views.generic.edit import UpdateView, CreateView
from mainapp.models import Stuff
from django.urls import reverse_lazy


class StuffUpdateView(UpdateView):
    model = Stuff
    template_name = 'adminapp/products/update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:products')

    def get_context_data(self, **kwargs):
        parent_context = super(StuffUpdateView, self).get_context_data(**kwargs)
        return parent_context

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(price=F)



class StuffCreateView(CreateView):
    model = Stuff
    template_name = 'adminapp/products/update.html'
    fields = ('__all__')
    success_url = reverse_lazy('adminapp:products')