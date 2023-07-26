
from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def login_views(request):
    formulario= LoginForms()

    if request.method == 'POST':
        if formulario.is_valid():

            nome=formulario['nome_login'].value()
            senha=formulario['senha'].value()

            usuario = auth.authenticate(
                request,
                usename= nome,
                password = senha
            )

            if usuario is not None:
                auth.login(request,usuario)
                messages.success(request,f'usuario {nome} logado com sucesso!')
                return redirect('cadastro:index')
            else:
                messages.error(request,'Erro ao tentar logar!')
                return redirect('usuario:login')


    return render(request,"usuario/paginas/usuario.html",context={'formulario':formulario})

def cadastro_views(request):
    formulario = CadastroForms()

    if request.method == "POST":
        formulario = CadastroForms(request.POST)
    
        if formulario.is_valid():
            if formulario['senha1'].value() == formulario['senha2'].value():
                messages.error(request,'As senhas não são iguais!')
                return redirect('usuario:cadastro')
    
            nome=formulario['nome_cadastro'].value()
            email=formulario['email_cadastro'].value()
            senha1=formulario['senha_1'].value()
            senha2= formulario['senha_2'].value()

            if User.objects.filter(username=nome,address=email,password1=senha1,password2=senha2).exists():
                return redirect('usuario:cadastro')

            novo_usuario = User.objects.create_user(

                username = nome,
                email = email,
                password1 = senha1,
                password2 = senha2
            )

            novo_usuario.save()
            return redirect('usuario:login')
    return render(request,"usuario/paginas/cadastro.html",context ={'formulario':formulario})

def logout(request):
    auth.logout(request)
    return redirect('usuario:loginpagina')

def usuario_head_views(request):
    return render(request,'usuario/parciais/usuario_head.html')

