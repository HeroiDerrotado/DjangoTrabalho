from django.shortcuts import render
from menu.models import Menu
from menu.models import Busca

# Create your views here.


def base_views(request):
    return render(request, 'menu/paginas/base.html')


def menu_views(request):
    return render(request, 'menu/paginas/menu_body.html')


def busca_views(request):
    template_name = 'busca.html'
    objects = Busca.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)
