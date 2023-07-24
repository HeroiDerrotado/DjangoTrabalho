from django.shortcuts import render
from vidamarinha.models import Curiosidade

# Create your views here.

def vidamarinha_views(request):
    return render(request,"vidamarinha/paginas/vidamarinha_body.html")

def busca_views(request):

    imagens = Curiosidade.objects.all()
    print(request)
    nome = request.GET['buscando']
    if nome:
        imagens = imagens.filter(nome_icontains=nome)
    return render(request,'vidamarinha/paginas/busca.html')

