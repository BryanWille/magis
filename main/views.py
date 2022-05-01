from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def sobre(request):
    return render(request, 'main/sobre.html')


def contato(request):
    return render(request, 'main/contato.html')
def quests(request):
    if request.session.get('usuario'):
        return HttpResponse('Logado')
    else:
        return redirect('/auth/login/?status=2')