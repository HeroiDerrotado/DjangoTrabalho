
from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def base_views(request):
    if not request.user.is_authenticated:
        messages.error(request,'usuario não logado')
        return redirect('usuario:loginpagina')
    return render(request,'ususario/paginas/base.html')

def base2_views(request):
    return render(request,'ususario/paginas/base2.html')

def login_views(request):
    
    formulario = LoginForms()

    if request.method == 'POST':
        formulario = LoginForms(request.POST)

        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha_login'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                return redirect('menuzin:menupagina')
            else:
                messages.error(request, 'Erro ao tentar logar!')
                return redirect('usuario:loginpagina')

    return render(request, "usuario/paginas/usuario.html", context={'formulario': formulario})

def cadastro_views(request):
    formulario = CadastroForms()

    if request.method == "POST":
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            if formulario['senha_cadastro1'] != formulario['senha_cadastro2'].value():
                return redirect('usuario:cadastropagina')

            nome = formulario['nome'].value()
            email = formulario['email'].value()
            senha1 = formulario['senha_cadastro1'].value()
            

            if User.objects.filter(username=nome).exists():
                return redirect('usuario:cadastropagina')

            novo_usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha1
            )

            novo_usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('usuario:loginpagina')

    return render(request, "usuario/paginas/cadastro.html", context={'formulario': formulario})

def logout(request):
    auth.logout(request)
    return redirect('usuario:loginpagina')
