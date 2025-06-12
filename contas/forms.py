from django.contrib.auth.forms import UserCreationForm

from django import forms
from contas.models import Usuario


class CriarContaForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Primeiro nome')
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')