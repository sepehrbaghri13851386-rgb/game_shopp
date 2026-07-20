from django import forms
from .models import coment

class ComentForm(forms.ModelForm):
    class Meta:
        model = coment
        fields = ['name', 'lastname', 'email', 'tiltle', 'discribshen']