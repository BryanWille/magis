from multiprocessing import context
from django.shortcuts import render

import questoes
from .models import *
from django.http import JsonResponse

app_name='questoes '

def home(request):
    materias = Materia.objects.all()
    context = {'materias': materias}
    return render(request, 'questoes/home.html', context)

def api_questao(request, id):
    perguntas_cruas = Questao.objects.filter(materia = id)[:20]
    questoes = []

    for pergunta_crua in perguntas_cruas:
        questao = {}
        questao['questao'] = pergunta_crua.questao
        questao['correta'] = pergunta_crua.correta
        questao['valor'] = pergunta_crua.valor

        opcoes = []

        opcoes.append(pergunta_crua.opcao_um)
        opcoes.append(pergunta_crua.opcao_dois)
        opcoes.append(pergunta_crua.opcao_tres)
        opcoes.append(pergunta_crua.opcao_quatro)
        opcoes.append(pergunta_crua.opcao_cinco)
        
        
        questao['opcoes'] = opcoes
        questoes.append(questao)

    return JsonResponse(questoes, safe=False)

def pega_questao(request, id):
    context = {'id': id}
    return render(request, 'questoes/questao.html', context)