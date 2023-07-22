from django.shortcuts import render
from usuario.form import LoginForms 

# Create your views here.

def login_views(request):
    formulario= LoginForms
    return render(request,"usuario/paginas/usuario.html",context={'formulario':formulario})

def cadastro_views(request):
    return render(request,"usuario/paginas/cadastro.html")
