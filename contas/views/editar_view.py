from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.shortcuts import reverse
from app.forms import SettingsForm
from contas.models import Usuario


# Create your views here.
class EditarPerfil(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "editarperfil.html"
    form_class = SettingsForm
    model = Usuario

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('app:home')