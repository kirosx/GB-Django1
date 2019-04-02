from django.forms import ModelForm
from mainapp.models import Category
from django import forms


class CategoryEdit(ModelForm):
    discount = forms.IntegerField(label='discount', required=False, min_value=0,max_value=90,initial=0)

    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ()

