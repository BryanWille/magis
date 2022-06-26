from tokenize import group
from unittest import mock
from django.shortcuts import render, redirect
from accounts.models import Users
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout


def login_attempt(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = Users.objects.filter(email=email).first()
        if not user:
            message = {'error': 'Usuario não existe!'}
            context = message
            return render(request, 'auth/login.html', context)
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            print("login")
            login(request, user)
            return redirect('home')
        else:
            message = {'error': 'Email ou senha invalidos!'}
            context = message
            return render(request, 'auth/login.html', context)
    return render(request, 'auth/login.html')

def register_attempt(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = Users.objects.filter(email=email).first()

        if user:
            message = {'error': 'Já existe esse usuario no sistema!'}
            context = message
            return render(request, 'auth/register.html', context)
        user = Users(first_name=f_name, last_name=l_name, email=email, username=email, cargo ="A")
        user.set_password(password)
        user.save()
    return render(request, 'auth/register.html')

@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Alunos'))



def logout_attempt(request):
    logout(request)
    return redirect('index')
