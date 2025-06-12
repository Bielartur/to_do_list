from django.shortcuts import reverse
from django.views.generic import FormView


class CriarConta(FormView):
    template_name = 'criar_conta.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contas:login')