from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from app.forms import ToDoListForm
from app.models import ToDoList

class Home(LoginRequiredMixin, FormMixin, ListView):
    model = ToDoList
    template_name = 'home.html'
    context_object_name = 'tasks'
    form_class = ToDoListForm
    success_url = reverse_lazy('app:home')

    def get_queryset(self):
        # Base: só as tasks do usuário
        qs = super().get_queryset().filter(user=self.request.user)
        filtros = {
            'concluidas': True,
            'pendentes': False,
        }
        filtro = self.request.GET.get('filtro')
        if filtro in filtros:
            qs = qs.filter(done=filtros[filtro])

        ordens = {
            'concluidas': 'done',
            'pendentes': '-done',
        }
        ordem = self.request.GET.get('ordem')
        if ordem in ordens:
            qs = qs.order_by(ordens[ordem])

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Instancia vazia do form para a área de criação
        ctx['form'] = self.get_form()
        # Para manter o select “selected” no template
        ctx['filtro'] = self.request.GET.get('filtro', '')
        ctx['ordem'] = self.request.GET.get('ordem', '')
        return ctx

    def post(self, request, *args, **kwargs):
        """
        Aqui nós tratamos:
         - criação de nova task (via FormMixin)
         - exclusão (task-delete)
         - toggle de done (task-done)
        """
        if 'task-delete' in request.POST:
            pk = int(request.POST['task-delete'])
            ToDoList.objects.filter(pk=pk, user=request.user).delete()
            return redirect(self.success_url)

        if 'task-done' in request.POST:
            pk, done = request.POST['task-done'].split(',')
            task = ToDoList.objects.get(pk=int(pk), user=request.user)
            task.done = not (done.lower() == 'true')
            task.save()
            return redirect(self.success_url)

        # Se não for delete nem toggle, assumimos criação de nova task
        form = self.get_form()
        if form.is_valid():
            ToDoList.objects.create(
                user=request.user,
                title=form.cleaned_data['task']
            )
            return redirect(self.success_url)
        else:
            # Em caso de erro no form, renderiza a lista + erros do form
            return self.form_invalid(form)
