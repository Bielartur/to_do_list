from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.shortcuts import reverse
from app.forms import ToDoForm

# Create your views here.
class Home(LoginRequiredMixin, FormView):
    template_name = 'home.html'
    form_class = ToDoForm

    def get_success_url(self):
        return reverse('app:home')