from django.urls import path
from .views import index, sobre, contato, quests


urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('quests/', quests, name='quests')
]
