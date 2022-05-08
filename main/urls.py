from django.urls import path
from .views import index, quests


urlpatterns = [
    path('', index, name='index.html'),
    path('quests/', quests, name='quests')
]
