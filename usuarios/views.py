from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as logar
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, "usuarios\cadastro.html")
    else:
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        user = User.objects.filter(username=usuario).first()

        if user:
            return HttpResponse("Já existe um usuário com esse nome.")

        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        return HttpResponse("Usuário cadastrado com sucesso.")
        

def login(request):
    if request.method == 'GET':
        return render(request, "usuarios\login.html")
    else:
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        
        user = authenticate(username=usuario, password=senha)

        if user:
            logar(request, user)
            return HttpResponse("Autenticado com sucesso!")
        else:
            return HttpResponse("Usuario ou senha inválido(s)")


@login_required(login_url="/auth/login/")
def plataforma(request): #Forma mais rápida
        return HttpResponse("plataforma")


#def plataforma(request): #teste
#    if request.user.is_authenticated:
#        return HttpResponse("Plataforma")
#    else:
#        return HttpResponse("Você precisa estar logado")