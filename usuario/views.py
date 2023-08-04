from usuario.form import LoginForms, CadastroForms, ImagemForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from usuario.models import Usuario, Imagem
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login

#NÃO CONSEGUIMOS CONECTAR PÁGINA DE CADASTRO COM O BANCO DE DADO; NÃO SALVA USUÁRIOS




@login_required(login_url='usuario:loginpagina')
def adiciona_views(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado na página')
        return redirect('usuario:loginpagina')
    
    formulario = ImagemForm()

    if request.method == 'POST':
        formulario = ImagemForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Nova imagem cadastrada')
            return redirect('usuario:basepagina')

    imagens = Imagem.objects.all() 
    return render(request, 'usuario/paginas/adicionar.html', context={'formulario': formulario, 'imagens': imagens})



def apaga_views(request, id_url):

    imagem = imagem[0]
    imagem.delete()
    messages.success(request, 'imagem apagada com suceso')

    return render(request, 'usuario/paginas/apaga.html', context={'id_url': id_url})

@login_required(login_url='usuario:loginpagina')
def edita_views(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado na página')
        return redirect('usuario:loginpagina')

    imagem = Usuario.objects.filter(id=id_url)
    if not imagem:
        messages.error(request, 'imagem não encontrada')
        return redirect('usuario:basepagina')

    imagem = imagem[0]
    formulario = ImagemForm(instance=imagem)
    if request.method == 'POST':
        formulario = ImagemForm(request.POST, request.FILES, instance=imagem)
        if fomulario.is_valid():
            formulario.save()
            messages.success(request, 'Imagem alterada')
            return redirect('usuario:basepagina')

    return render(request, 'usuario/paginas/edita.html', context={'formulario': formulario, 'id_da_imagem': id_url})


def outra_view(request):
    id_da_imagem = 1
    url_editar_imagem = reverse('editar_imagem', args=[id_da_imagem])

    return render(request, "usuario/paginas/outra.hrml", context={"url_editar_imagem": url_editar_imagem})


def base_views(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("usuario:loginpagina")
    return render(request, 'usuario/paginas/base.html')


def login_views(request):
      
    formulario = LoginForms()

    if request.method == "POST":
        formulario = LoginForms(request.POST)
        if formulario.is_valid():
            nome = formulario.cleaned_data['nome_login']
            senha = formulario.cleaned_data['senha_login']

            usuario = authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, f"Usuário {nome} logado com sucesso")
                return redirect('menuzin:menupagina')
            else:
                messages.error(request, 'Erro ao tentar logar')
                return redirect('usuario:loginpagina')

    return render(request, 'usuario/paginas/usuario.html', {'formulario': formulario})




def cadastro_views(request):
    formulario = CadastroForms()

    if request.method == "POST":
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            if formulario.cleaned_data['senha1'] != formulario.cleaned_data["senha2"]:
                messages.error(request, "As senhas não são iguais")
                return redirect("usuario:cadastropagina")

            nome = formulario.cleaned_data["username"]
            email = formulario.cleaned_data["email"]
            senha = formulario.cleaned_data["password"]

            if User.objects.filter(username=nome).exists():
                messages.error(request, "O usuário já existe")
                return redirect("usuario:cadastropagina")

            novo_usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            novo_usuario.save()


            novo_usuario = Usuario(user=novo_usuario)
            novo_usuario.save()

            messages.success(request, "Cadastro realizado com sucesso")
            return redirect("usuario:loginpagina")

    return render(request, "usuario/paginas/cadastro.html", {'formulario': formulario})


def logout_view(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('usuario:loginpagina')
