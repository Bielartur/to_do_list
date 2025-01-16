
from django.urls import path
from app_to_do.views import home
from contas.views import login, cadastro_usuario

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
]
