
from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse


def base_views(request):
    if request.user.is_authenticated:
        return render(request, 'ususario/paginas/base.html')


def base2_views(request):

    if request.user.is_authenticated:
        return render(request, 'usuario/paginas/base2.html')


def login_views(request):

    formulario = LoginForms

    if request.method == "GET":
        return render(request, "usuario/paginas/usuario.html")
    else:
        nome = formulario(request.POST.get("username",))
        senha = formulario(request.POST.get("senha",))

        user = authenticate(request, username=nome, password=senha)

        if user:
            login_views(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse("senha ou nome invalidos")

    return


def cadastro_views(request):

    formulario = CadastroForms

    if request.method == 'GET':
        return render(request, 'usuario/paginas/cadastro.html')
    else:
        username = formulario(request.POST.get("username",))
        senha = formulario(request.POST.get("senha",))

        user = User.objects.get(username=username)

        if user:
            return HttpResponse("Já existe um usuario com esse nome")

        user = User.objects.get(username=username, password=senha)
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")


def logout(request):
    authenticate.logout(request)
    return redirect('usuario:loginpagina')
