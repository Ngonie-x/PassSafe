from django.urls import path
from .views import password_index

app_name = 'passwordsapp'

urlpatterns = [
    path('', password_index, name="home"),
]