from django.db import models
from usuarios.models import Usuario

class Materia(models.Model):
    nome_materia = models.CharField(max_length=100)

    class Meta:
        ordering = ('nome_materia',)
        verbose_name = 'matéria'
        verbose_name_plural = 'matérias'

    def __str__(self):
        return self.nome_materia

class Questao(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    questao = models.CharField(max_length=300)
    resposta = models.IntegerField()
    opcao_um = models.CharField(max_length=100)
    opcao_dois = models.CharField(max_length=100)
    opcao_tres = models.CharField(max_length=100)
    opcao_quatro = models.CharField(max_length=100)
    opcao_cinco = models.CharField(max_length=100)

    marks = models.IntegerField(default=5)

    class Meta:
        ordering = ('questao',)
        verbose_name = 'questão'
        verbose_name_plural = 'questões'

    def __str__(self):
        return self.questao

class Placar(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    placar = models.IntegerField()