from django.forms import EmailField
from django.shortcuts import render

<<<<<<< HEAD
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
            redirect('')
        else:
            message = {'error': 'Email ou senha incorreto(s)!'}
            context = message
            return render(request, "usuarios/login.html", context)
    return render(request, "usuarios/login.html")
=======
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    status = request.GET.get('status')
    return render(request, "usuarios\login.html", {"status":status})
>>>>>>> parent of c5ed203 (Login com allauth funcionando)

def cadastro(request):
    status = request.GET.get('status')
    return render(request, "usuarios\cadastro.html", {"status":status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    existe = Usuario.objects.filter(email = email)
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) <= 8:
        return redirect('/auth/cadastro/?status=2')

    if len(existe) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
<<<<<<< HEAD
        message = {'success': 'Usuário cadastrado com sucesso!'}
        context = message
    return render(request, "usuarios/cadastro.html", context)
=======
        return redirect('/auth/cadastro/?status=0')
        
    except:
        redirect('/auth/cadastro/?status=4')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/quests/?id_ususario={request.session["usuario"]}')


def sair(request):
    request.session.flush()
    return redirect('/auth/login')
>>>>>>> parent of c5ed203 (Login com allauth funcionando)

