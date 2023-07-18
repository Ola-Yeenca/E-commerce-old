from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Username"
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Email"
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Password"
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Confirm Password"
        }
    ))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Username"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w-full px-2 py-4 rounded-xl',
            'placeholder': "Password"
        }
    ))


class LogoutForm(forms.Form):
    pass
