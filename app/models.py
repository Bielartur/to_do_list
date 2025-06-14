from django.db import models

from contas.models import Usuario

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
