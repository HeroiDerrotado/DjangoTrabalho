
from django.shortcuts import render
from usuario.form import ImagemForm
from menu.models import Busca  

# Create your views here.


def base_views(request):
    return render(request, 'menu/paginas/base.html')


def menu_views(request):
    return render(request, 'menu/paginas/menu_body.html')



def busca_imagem(request):
    if request.method == 'POST':
        formulario = ImagemForm(request.POST)
        if formulario.is_valid():
            termo_busca = formulario.cleaned_data['termo_busca']
            imagens = Busca.objects.filter(titulo__icontains=termo_busca)
            return render(request, 'resultado_busca.html', {'imagens': imagens, 'termo_busca': termo_busca})
    else:
        formulario = ImagemForm()
    return render(request, 'menu/paginas/busca.html', {'formulario': formulario})
