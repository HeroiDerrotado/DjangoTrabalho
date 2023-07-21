from django.shortcuts import render
from pesca.models import Imagem

# Create your views here.

def pesca_views(request):
    return render(request,"pesca/paginas/pesca_body.html")

def views_busca(request):

    imagens = Imagem.objects.all()
    print(request)

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            imagens = imagens.filter(nome__icontains=nome)

    return render(request, 'pesca/paginas/busca.html', context ={'imagens' : imagens})
