from django.shortcuts import render

# Create your views here.

def menu_views(request):
    return render(request,'menu/paginas/menu.html')
