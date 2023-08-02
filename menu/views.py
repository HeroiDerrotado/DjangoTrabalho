from django.shortcuts import render
from menu.models import Menu
from menu.models import Busca

# Create your views here.


def base_views(request):
    return render(request,'menu/paginas/base.html')

def menu_views(request):
    return render(request,'menu/paginas/menu_body.html')

def views_busca(request):
    imagens = Menu.objects.all()
    form = Busca()

    if 'buscando' in request.GET:
        form = Busca(request.GET)
        if form.is_valid():
            nome = form.cleaned_data['buscando']
            if nome:
                imagens = imagens.filter(nome__icontains=nome)

    return render(request, 'menu/paginas/busca.html', {'imagens': imagens, 'form': form})
