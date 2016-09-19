from django import forms
from django.core import validators

from example_project.apps.example_app.models import Example

class NewExampleForm(forms.ModelForm):

    class Meta:
        model = Example
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
