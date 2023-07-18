from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Item

INPUT_CLASSES = 'w-mid py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price',  'image']

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
                }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Name'
                }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Description'
                }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Price'
                }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Image'
                }),
        }
