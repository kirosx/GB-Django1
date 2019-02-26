from django.forms import ModelForm
from mainapp.models import Stuff

class ProductEdit(ModelForm):
    class Meta:
        model = Stuff
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductEdit, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''