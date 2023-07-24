
from usuario.form import LoginForms, CadastroForms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
                return redirect('cadastro:index')
            else:
                return redirect('usuario:login')


    return render(request,"usuario/paginas/usuario.html",context={'formulario':formulario})

def cadastro_views(request):
    formulario = CadastroForms()

    if request.method == "POST":
        formulario = CadastroForms(request.POST)
    
        if formulario.is_valid():
            if formulario['senha1'].value() == formulario['senha2'].value():
                return redirect('usuario:cadastro')
    
            nome=formulario['nome_cadastro'].value()
            email=formulario['email_cadastro'].value()
            senha=formulario['senha_1'].value()
            senha= formulario['senha_2'].value()

        if User.objects.filter(username=nome).exists():
            return redirect('usuario:cadastro')

        novo_usuario = User.objects.create_user(

            username = nome,
            email = email,
            password = senha
        )

        novo_usuario.save()
        return redirect('usuario:login')
    return render(request,"usuario/paginas/cadastro.html",context ={'formulario':formulario})
