from django.urls import path
from .views import index, quests


urlpatterns = [
    path('', index, name='index'),
    path('quests/', quests, name='quests')
]
