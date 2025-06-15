from django import forms
from django.contrib.auth.forms import UserChangeForm

from contas.models import Usuario


class ToDoListForm(forms.Form):
    task = forms.CharField(label='')

class SettingsForm(UserChangeForm):
    first_name = forms.CharField(label='Primeiro nome')
    last_name = forms.CharField(label='Último nome')
    email = forms.EmailField(label='Email')

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email')
