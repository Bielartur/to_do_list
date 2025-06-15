from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view

from contas.views.criar_conta_view import CriarConta
from contas.views.editar_view import EditarPerfil

app_name = 'contas'

urlpatterns = [
    path('criarconta/', CriarConta.as_view(), name='criar_conta'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('editarperfil/<int:pk>', EditarPerfil.as_view(), name='editar_perfil'),
    path('mudarsenha/<int:pk>', auth_view.PasswordChangeView.as_view(
        template_name='mudarsenha.html',
        success_url=reverse_lazy('app:home')),
        name='mudar_senha')
]