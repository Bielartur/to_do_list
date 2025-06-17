from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from contas.models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
            model = Usuario
            fields = ('email',)

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"autofocus": True, "autocomplete": "email"}
        )
    )

class CriarContaForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Primeiro nome')
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
