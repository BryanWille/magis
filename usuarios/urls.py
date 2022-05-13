from django.urls import path
from .views import cadastro, login1

urlpatterns = [
    path("login/", login1, name="login1"),
    path("cadastro/", cadastro, name="cadastro")
    #path("valida_cadastro", valida_cadastro, name="valida_cadastro"),
    #path("valida_login", valida_login, name="valida_login"),
    #path("logout/", logout, name="logout")
]