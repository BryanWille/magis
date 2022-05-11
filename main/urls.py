from django.urls import path
<<<<<<< Updated upstream
from .views import index, quests
=======
from .views import index, sobre, contato
>>>>>>> Stashed changes


urlpatterns = [
    path('', index, name='index'),
<<<<<<< Updated upstream
    path('quests/', quests, name='quests')
=======
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
>>>>>>> Stashed changes
]
