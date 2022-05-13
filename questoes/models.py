from django.db import models

class Materia(models.Model):

    nome = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.nome

class Questao(models.Model):
    
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
    questao = models.CharField(max_length=1000)
    correta = models.PositiveSmallIntegerField()
    opcao_um = models.CharField(max_length=100)
    opcao_dois = models.CharField(max_length=100)
    opcao_tres = models.CharField(max_length=100)
    opcao_quatro = models.CharField(max_length=100)
    opcao_cinco = models.CharField(max_length=100)

    valor = models.IntegerField(default=5)

    def __str__(self):
        return self.questao
