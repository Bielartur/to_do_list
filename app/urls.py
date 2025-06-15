from django.urls import path
from app.views.home_view import Home

app_name = 'app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tasks/<int:pk>/delete/', Home.as_view(), name='tasks'),
]
