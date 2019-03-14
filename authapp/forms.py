from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import CustomUser, CustomUserProfile
import random, hashlib

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'age', 'first_name','email')

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text=''

    def save(self):
        user = super(RegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name in ('password','is_staff','is_superuser'):
                field.widget = forms.HiddenInput()


class CustomUserProfileEditForm(forms.ModelForm):
    class Meta:
        model= CustomUserProfile
        fields = ('tagline','about_me','gender')

    def __init__(self, *args, **kwargs):
        super(CustomUserProfileEditForm,self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']='form-control'
