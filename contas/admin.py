from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioCreationForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    model    = Usuario

    # mostra os campos no list view do admin
    list_display = ("email", "is_staff", "is_active")
    ordering     = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        }),
    )
