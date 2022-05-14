from django.urls import path
from .views import cadastro, login, valida_cadastro, valida_login, sair

urlpatterns = [
<<<<<<< HEAD
    path("login/", login1, name="login1"),
    path("cadastro/", cadastro, name="cadastro")
=======
    path("login/", login, name="login1"),
    path("cadastro/", cadastro, name="cadastro"),
    path("valida_cadastro", valida_cadastro, name="valida_cadastro"),
    path("valida_login", valida_login, name="valida_login"),
    path("sair/", sair, name="sair")
>>>>>>> parent of c5ed203 (Login com allauth funcionando)
]