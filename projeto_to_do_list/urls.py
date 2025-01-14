
from django.urls import path
from app_to_do import views

urlpatterns = [
    path('', views.home, name='home'),
]
