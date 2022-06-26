from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    is_staff = models.BooleanField(
        ('staff status'),
        default=True
    )

    choices_cargo = (('D', 'Diretoria'),
                     ('P','Professor'),
                     ('A', 'Aluno'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)
