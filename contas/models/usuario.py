from django.contrib.auth.models import AbstractUser
from django.db import models

from contas.models.usuario_manager import UsuarioManager


# Create your models here.
class Usuario(AbstractUser):
    username = None  # Anula o campo herdado
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
