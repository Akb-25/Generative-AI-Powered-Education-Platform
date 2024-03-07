from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class LoginForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    country=forms.CharField(label="Country Name",max_length=50)
    gender=forms.CharField(label="Gender",max_length=10)

    class Meta:
        model = User
        fields=["username","email","password1","password2"]

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ["full_name", "country", "gender", "username", "email", "password1", "password2"]

#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.fields['password1'].widget = forms.PasswordInput()
#         self.fields['password2'].widget = forms.PasswordInput()