from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('view_score', view_score, name="view_score"),
    path('api/check_score', check_score, name="check_score"),
    path('<id>', take_quiz, name="take_quiz"),
    path('api/<id>', api_question, name="api_question"),
    path('api/get-quiz/', get_quiz, name="get_quiz"),
    path('quiz/', quiz, name="quiz"),

]