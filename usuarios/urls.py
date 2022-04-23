from django.urls import path
from .views import cadastro, login, plataforma

urlpatterns = [
    path("cadastro/", cadastro, name="cadastro"),
    path("login/", login, name="login"),
    path("plataforma/", plataforma, name="plataforma")
]