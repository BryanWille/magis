from django.urls import path
from .views import cadastro, login1

urlpatterns = [
    path("login/", login1, name="login1"),
    path("cadastro/", cadastro, name="cadastro")
]