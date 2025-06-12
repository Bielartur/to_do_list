from django.urls import path
from django.contrib.auth import views as auth_views

from contas.views import CriarConta

app_name = 'contas'

urlpatterns = [
    path('criarconta/', CriarConta.as_view(), name='criar_conta'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]