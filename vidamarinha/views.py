from django.shortcuts import render
from vidamarinha.models import Curiosidade

# Create your views here.

def vidamarinha_views(request):
    return render(request,"vidamarinha/paginas/vidamarinha_body.html")

