from authapp.models import CustomUser
from django.forms import ModelForm

class UserEdit(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'