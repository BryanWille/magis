from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<id>', pega_questao, name="pega_questao"),
    path('api/<id>', api_questao, name="api_questao")
]
