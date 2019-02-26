from django.forms import ModelForm
from mainapp.models import Category


class CategoryEdit(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'