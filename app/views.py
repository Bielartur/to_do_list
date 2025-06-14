from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.shortcuts import reverse, redirect
from app.forms import ToDoListForm
from app.models import ToDoList


# Create your views here.
class Home(LoginRequiredMixin, FormView):
    template_name = 'home.html'
    form_class = ToDoListForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        tasks = ToDoList.objects.filter(user_id=request.user.id).all()
        return render(request, self.template_name, {'form': form,'tasks': tasks})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            ToDoList.objects.create(user=request.user, title=form.cleaned_data['task'])

        if request.POST.get('task-delete'):
            id = int(request.POST.get('task-delete'))
            ToDoList.objects.get(id=id).delete()

        if request.POST.get('task-done'):
            id, done = request.POST.get('task-done').split(',')
            task = ToDoList.objects.get(id=int(id))
            is_done = done.lower() == 'true'
            task.done = not is_done
            task.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('app:home')