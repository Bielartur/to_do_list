from django.urls import path
from app.views import Home

app_name = 'app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('editarperfil/', EditarPerfil.as_view(), name='editar_perfil'),
]
