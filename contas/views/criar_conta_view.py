from django.shortcuts import reverse
from django.views.generic import FormView

from contas.forms import CriarContaForm


class CriarConta(FormView):
    template_name = 'criar_conta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # 3) Quando o form NÃO for válido, re-renderiza o template
        #    incluindo form.errors no contexto
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('contas:login')