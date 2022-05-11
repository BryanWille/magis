from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('quest/', home, name="home"),
    path('<id>', pega_questoes, name="pega_questoes"),
    path('api/<id>', api_questao, name='api_questao'),
]