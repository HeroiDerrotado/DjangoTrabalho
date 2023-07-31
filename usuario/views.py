from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from usuario.models import Usuario  # Importe o modelo Usuario do arquivo models.py

def base_views(request):
    if request.user.is_authenticated:
        return render(request, 'usuario/paginas/base.html')
    else:
        return HttpResponse("Acesso não autorizado. Faça login primeiro.")

def base2_views(request):
    if request.user.is_authenticated:
        return render(request, 'usuario/paginas/base2.html')
    else:
        return HttpResponse("Acesso não autorizado. Faça login primeiro.")

def login_views(request):
    formulario = LoginForms(request.POST or None)

    if request.method == "POST" and formulario.is_valid():
        username = formulario.cleaned_data.get("username")
        password = formulario.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('Autenticado com sucesso.')
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")
            return redirect('usuario:loginpagina')

    return render(request, "usuario/paginas/usuario.html", {'formulario': formulario})

def cadastro_views(request):
    formulario = CadastroForms(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        username = formulario.cleaned_data.get("username")
        password = formulario.cleaned_data.get("senha")
        email = formulario.cleaned_data.get("email")

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "Já existe um usuário com esse nome.")
            return redirect('usuario:cadastropagina')

        # Crie o novo usuário com a senha criptografada
        user = Usuario(username=username, senha=password, email=email)
        user.save()

        # Faça login após o cadastro bem-sucedido
        login(request, user)
        return HttpResponse('Autenticado com sucesso após o cadastro.')

    return render(request, 'usuario/paginas/cadastro.html', {'formulario': formulario})

def logout_view(request):
    logout(request)
    return redirect('usuario:loginpagina')
