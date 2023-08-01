from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
# Importe o modelo Usuario do arquivo models.py
from django.contrib.auth.models import User


def base_views(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado")
        return redirect("usuario:loginpagina")
    return render(request, 'usuario/paginas/base.html')


def login_views(request):

    formulario = LoginForms()

    if request.method == "POST":
        formulario = LoginForms(request.POST)
        if formulario.is_valid():

            nome = formulario['nome_login'].value()
            senha = formulario['senha_login'].value()

            usuario = auth.authenticate(
                request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"usuario{nome}logado com sucesso")
                return redirect('menuzin:menupagina')
        else:
            messages.error(request, 'erro ao tentar logar')
            return redirect('usuario:loginpagina')

    return render(request, 'usuario/paginas/usuario.html', {'formulario': formulario})


def cadastro_views(request):

    formulario = CadastroForms()

    if request.method == "POST":
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            if formulario['senha1'].value() == formulario["senha2"].value():
                messages.error(request, "As senhas não são iguais")
                return redirect("usuario:cadastropagina")

            nome = formulario["nome_cadastro"].value()
            email = formulario["email_cadastro"].value()
            senha = formulario["senha_cadastro1"].value()

            if User.objects.filter(nome=nome, email=email, senha=senha).exists():
                messages.error(request, "O usario já existe")
                return redirect("usuario:cadastropagina")

            novo_usuario = User.objects.create_user(
                username=nome,
                email=email,
                senha=senha
            )

            novo_usuario.save()
            messages.success(request, "Cadastro realizado com sucesso")
            return redirect("usuario:loginpagina")

    return render(request, "usuario/paginas/cadastro.html", {'formulario': formulario})


def logout_view(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('usuario:loginpagina')
