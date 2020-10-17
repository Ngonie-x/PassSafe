from django.urls import path
from .views import user_login, register
from django.contrib.auth.views import LogoutView


app_name = 'accounts'

urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout')

]
