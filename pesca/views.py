from django.shortcuts import render
from pesca.models import Pesca

# Create your views here.

def pesca_views(request):
    return render(request,"pesca/paginas/pesca_body.html")

