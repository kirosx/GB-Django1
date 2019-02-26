from django.views.generic.edit import UpdateView
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