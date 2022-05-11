from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse


def home(request):
    if request.session.get('usuario'):
        materias = Materia.objects.all()
        context = {'materias': materias}
        return render(request, 'questoes\home.html', context)
    else:
        return redirect('/auth/login/?status=2')

def api_questao(request, id):
        perguntas_cruas = Questao.objects.filter(materia=id)[:20]
        questoes = []

        for pergunta_crua in perguntas_cruas:
            questao = {}
            questao['id'] = pergunta_crua.id
            questao['questao'] = pergunta_crua.questao
            questao['resposta'] = pergunta_crua.resposta
            questao['marks'] = pergunta_crua.marks

            opcoes = []
            opcoes.append(pergunta_crua.opcao_um)
            opcoes.append(pergunta_crua.opcao_dois)
            opcoes.append(pergunta_crua.opcao_tres)
            opcoes.append(pergunta_crua.opcao_quatro)
            opcoes.append(pergunta_crua.opcao_cinco)

            questao['opcoes'] = opcoes

            questoes.append(questao)

        return JsonResponse(questoes, safe=False)



def pega_questoes(request, id):
    context = {'id': id}
    return render(request, 'questoes\questoes.html', context)


