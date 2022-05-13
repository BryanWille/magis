from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def sobre(request):
    return render(request, 'main/sobre.html')


def contato(request):
    return render(request, 'main/contato.html')

