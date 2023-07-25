from django.shortcuts import render
from especies.models import EspecieGeral

# Create your views here.

def especies_views(request):
    return render(request,"especies/paginas/especies_body.html")

def busca_views(request):

    imagens = EspecieGeral.objects.all()
    print(request)

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            imagens =imagens.filter(nome_icontains= nome)
    return render(request,'especies/paginas/busca.html',context={'imagens':imagens})


