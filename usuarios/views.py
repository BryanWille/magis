from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login 

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(email = email).first()
        if not user:
            message = {'error': 'Usuário não existe!'}
            context = message
            return render(request, "usuarios/login.html", context)
        user = authenticate(username=email, password=senha)
        print(user)
        if user is not None:
            login(request, user)
            redirect('questoes/home.html')
        else:
            message = {'error': 'Email ou senha incorreto(s)!'}
            context = message
            return render(request, "usuarios/login.html", context)
    return render(request, "usuarios/login.html")

def cadastro(request):
    if request.method == 'POST':
        p_nome = request.POST.get('p_nome')
        u_nome = request.POST.get('u_nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(email = email).first()

        if user:
            message = {'error': 'Usuário já existe!'}
            context = message
            return render(request, "usuarios/cadastro.html", context)

        usuario = User(first_name = p_nome, last_name = u_nome, email= email, username = email)
        usuario.set_password(senha)
        usuario.save()
    return render(request, "usuarios/cadastro.html")

