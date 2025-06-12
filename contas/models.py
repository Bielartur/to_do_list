from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    first_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
