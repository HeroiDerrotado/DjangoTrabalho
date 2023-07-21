from django.shortcuts import render
from vidamarinha.models import Imagem

# Create your views here.

def vidamarinha_views(request):
    return render(request,"vidamarinha/paginas/vidamarinha_head.html")

def busca_views(request):

    imagens = Imagem.objects.all()
    print(request)
    nome = request.GET['buscando']
    if nome:
        imagens = imagens.filter(nome_icontains=nome)
    return render(request,'vidamarinha/paginas/busca.html')

